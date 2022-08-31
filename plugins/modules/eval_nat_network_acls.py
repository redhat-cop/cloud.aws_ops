#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: eval_nat_network_acls
short_description: Evaluate ingress and egress NAT netwok ACLs
description:
  - Evaluate ingress and egress NAT netwok ACLs.
  - Confirms whether the NACLs allow the needed traffic between the source and destination resources.
author:
  - Alina Buzachis (@alinabuzachis)
options:
  src_ip:
    description:
    - The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
    type: str
    required: true
  src_subnet_id:
    description:
    - Source Subnet id.
    type: str
    required: true
  src_port_range:
    description:
    - The port range used by the AWS resource in your Amazon VPC you want to test connectivity from.
    type: str
    required: false
  dst_ip:
    description:
    - The IPv4 address of the resource you want to connect to.
    type: str
    required: true
  dst_port:
    description:
    - The port number you want to connect to on the destination resource.
    type: str
    required: true
  nat_subnet_id:
    description:
    - NAT Subnet id.
    type: str
    required: true
  nat_network_acls:
    description:
    - NAT network ACLs.
    type: list
    elements: dict
    required: true
  routes:
    description:
    - NAT routes.
    type: list
    elements: dict
    required: true
"""


EXAMPLES = r"""
- name: Evaluate ingress and egress NAT netwok ACLs
  eval_nat_network_acls:
    ...

"""


RETURN = r"""
result:
  type: str
  description: Results from evaluating NAT network ACLS.
  returned: success
  sample: 'NAT Network ACLs evaluation successful'
"""


from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class EvalNatNetworkAcls(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            src_ip=dict(type="str", required=True),
            src_port_range=dict(type="str", required=True),
            src_subnet_id=dict(type="str", required=True),
            dst_ip=dict(type="str", required=True),
            dst_port=dict(type="str", required=True),
            nat_subnet_id=dict(type="str", required=True),
            nat_network_acls=dict(type="list", elements="dict", required=True),
            routes=dict(type="list", elements="dict", required=True),
        )

        super(EvalNatNetworkAcls, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def eval_nat_nacls(self):
        src_ip = ip_address(self.src_ip)
        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)
        src_port_from = None
        src_port_to = None
        # entry list format
        keys = [
            "rule_number",
            "protocol",
            "rule_action",
            "cidr_block",
            "icmp_type",
            "icmp_code",
            "port_from",
            "port_to",
        ]
        if self.src_port_range:
            src_port_from = int(self.src_port_range.split("-")[0])
            src_port_to = int(self.src_port_range.split("-")[1])

        egress_acls = [acl["egress"] for acl in self.nat_network_acls if acl["egress"]][
            0
        ]
        ingress_acls = [
            acl["ingress"] for acl in self.nat_network_acls if acl["ingress"]
        ][0]

        def check_egress_towards_dst(acls, dst_ip, dst_port):
            for item in acls:
                acl = dict(zip(keys, item))
                # Check ipv4 acl rule only
                if acl.get("cidr_block"):
                    # Check IP
                    if dst_ip in ip_network(acl["cidr_block"], strict=False):
                        # Check Port
                        if (acl.get("protocol") == "all") or (
                            dst_port
                            in range(
                                acl["port_from"],
                                acl["port_to"] + 1,
                            )
                        ):
                            # Check Action
                            if acl["rule_action"] == "allow":
                                return True
                            else:
                                self.fail_json(
                                    msg=f"NatGateway Subnet {self.src_subnet_id} Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(dst_port)}"
                                )
            else:
                self.fail_json(
                    msg=f"NatGateway Subnet {self.src_subnet_id} Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(dst_port)}"
                )

        def check_ingress_from_dst(acls, src_ip):
            for item in acls:
                acl = dict(zip(keys, item))
                # Check ipv4 acl rule only
                if acl.get("cidr_block"):
                    # Check IP
                    if src_ip in ip_network(acl["cidr_block"], strict=False):
                        # Check Port
                        if (acl.get("protocol") == "all") or (
                            src_port_from
                            and src_port_to
                            and set(range(src_port_from, src_port_to)).issubset(
                                range(
                                    acl["port_from"],
                                    acl["port_to"] + 1,
                                )
                            )
                        ):
                            # Check Action
                            if acl["rule_action"] == "allow":
                                return True
                            else:
                                self.fail_json(
                                    msg=f"NatGateway Subnet {self.src_subnet_id} Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                                )
            else:
                self.fail_json(
                    msg=f"NatGateway Subnet {self.src_subnet_id} Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                )

        def check_ingress_from_src(acls, src_ip, dst_port):
            for item in acls:
                acl = dict(zip(keys, item))
                # Check ipv4 acl rule only
                if acl.get("cidr_block"):
                    # Check IP
                    if src_ip in ip_network(acl["cidr_block"], strict=False):
                        # Check Port
                        if (acl.get("protocol") == "all") or (
                            dst_port
                            in range(
                                acl["port_from"],
                                acl["port_to"] + 1,
                            )
                        ):
                            # Check Action
                            if acl["rule_action"] == "allow":
                                return True
                            else:
                                self.fail_json(
                                    msg=f"NatGateway Subnet Network Acl Ingress Rules do not allow inbound traffic from source: {self.src_ip} towards destination port {str(dst_port)}"
                                )
            else:
                self.fail_json(
                    msg=f"NatGateway Subnet Network Acl Ingress Rules do not allow inbound traffic from source {self.src_ip} towards destination port {str(dst_port)}"
                )

        def check_egress_towards_src(acls, dst_ip):
            for item in acls:
                acl = dict(zip(keys, item))
                # Check ipv4 acl rule only
                if acl.get("cidr_block"):
                    # Check IP
                    if dst_ip in ip_network(acl["cidr_block"], strict=False):
                        # Check Port
                        if (acl.get("protocol") == "all") or (
                            src_port_from
                            and src_port_to
                            and set(range(src_port_from, src_port_to)).issubset(
                                range(
                                    acl["port_from"],
                                    acl["port_to"] + 1,
                                )
                            )
                        ):
                            # Check Action
                            if acl["rule_action"] == "allow":
                                return True
                            else:
                                self.fail_json(
                                    msg=f"NatGateway Subnet Network Acl Egress Rules do not allow outbound traffic to source: {self.src_ip}"
                                )
            else:
                self.fail_json(
                    msg=f"NatGateway Subnet Network Acl Egress Rules do not allow outbound traffic to source: {self.src_ip}"
                )

        check_egress_towards_dst(egress_acls, dst_ip, dst_port)
        check_ingress_from_dst(ingress_acls, dst_ip)

        if self.src_subnet_id == self.nat_subnet_id:
            return True

        check_ingress_from_src(ingress_acls, src_ip, dst_port)
        check_egress_towards_src(egress_acls, src_ip)

        return True

    def get_nat_next_hop(self):
        destination = ip_address(self.dst_ip)
        most_specific = -1

        if self.src_subnet_id == self.nat_subnet_id:
            self.fail_json(
                msg="NatGateway and Source cannot be placed in the same subnet, NatGateway should be in a public subnet"
            )

        for route in self.routes:
            # Confirms whether the source has a public IP address associated with the resource, if the route destination is an internet gateway.
            if route.get("destination_cidr_block"):
                mask = int(route["destination_cidr_block"].split("/")[1])
                if (
                    not "destination_prefix_list_id" in str(route)
                    and destination
                    in ip_network(route["destination_cidr_block"], strict=False)
                    and mask > most_specific
                ):
                    if route["state"] != "blackhole":
                        most_specific = mask
                        next_hop = route
        # 0.0.0.0/0
        if most_specific >= 0 and "igw-" in str(next_hop):
            return True
        self.fail_json(
            msg=f"No Internet Gateway route found for destination: {self.dst_ip}"
        )

    def execute_module(self):
        try:
            # Evaluate ingress and egress NAT netwok ACLs
            self.eval_nat_nacls()
            self.get_nat_next_hop()
            self.exit_json(result="NAT Network ACLs evaluation successful")
        except Exception as e:
            self.fail_json(
                msg="NAT Network ACLs evaluation failed: {}".format(e), exception=e
            )


def main():

    EvalNatNetworkAcls()


if __name__ == "__main__":
    main()
