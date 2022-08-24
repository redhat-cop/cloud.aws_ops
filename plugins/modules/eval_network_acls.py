#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: eval_network_acls
short_description: Evaluate ingress and egress netwok ACLs
description:
  - Evaluate ingress and egress netwok ACLs.
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
  dst_subnet_id:
    description:
    - Destination Subnet id.
    type: str
    required: true
  src_network_acls:
    description:
    - Source Network ACL Rules.
    type: dict
    required: true
  dst_network_acls:
    description:
    - Destination Network ACL Rules.
    type: dict
    required: true
"""

EXAMPLES = r"""
- name: Evaluate ingress and egress netwok ACLs
  eval_network_acls:
    ...

"""

RETURN = r"""
result:
  type: str
  description: Results from evaluating ingress and egress netwok ACLs.
  returned: success
  sample: 'Network ACLs evaluation successful'
"""

from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class EvalNetworkAcls(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            src_ip=dict(type="str", required=True),
            src_subnet_id=dict(type="str", required=True),
            src_port_range=dict(type="str", required=False),
            dst_ip=dict(type="str", required=True),
            dst_subnet_id=dict(type="str", required=True),
            dst_port=dict(type="str", required=True),
            src_network_acls=dict(type="dict", required=True),
            dst_network_acls=dict(type="dict", required=True),
        )

        super(EvalNetworkAcls, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def eval_nacls(self):
        if self.src_port_range:
            src_port_from = int(self.src_port_range.split("-")[0])
            src_port_to = int(self.src_port_range.split("-")[1])
        src_ip = ip_address(self.src_ip)
        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)

        if self.src_subnet_id == self.dst_subnet_id:
            return True

        def eval_src_nacls(acls):
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

            def check_egress_acls(acls, dst_ip, dst_port):
                for item in acls:
                    acl = dict(zip(keys, item))
                    # Check ipv4 acl rule only
                    if acl.get("cidr_block"):
                        # Check IP
                        if dst_ip in ip_network(acl["cidr_block"], strict=False):
                            # Check Port
                            if (acl.get("protocol") == "-1") or (
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
                                        msg=f"Source Subnet Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(dst_port)}"
                                    )
                else:
                    self.fail_json(
                        msg=f"Source Subnet Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(dst_port)}"
                    )

            def check_ingress_acls(acls, src_ip):
                for item in acls:
                    acl = dict(zip(keys, item))
                    # Check ipv4 acl rule only
                    if acl.get("cidr_block"):
                        # Check IP
                        if src_ip in ip_network(acl["cidr_block"], strict=False):
                            # Check Port
                            if (acl.get("protocol") == "-1") or (
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
                                        msg=f"Source Subnet Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                                    )
                else:
                    self.fail_json(
                        msg=f"Source Subnet Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                    )

            egress_acls = [acl for acl in acls["nacls"] if acl["egress"]]
            ingress_acls = [acl for acl in acls["nacls"] if not acl["egress"]]


            src_egress_check_pass = check_egress_acls(egress_acls, dst_ip, dst_port)
            src_ingress_check_pass = check_ingress_acls(ingress_acls, dst_ip)

            if src_ingress_check_pass and src_egress_check_pass:
                return True

        def eval_dst_nacls(acls):
            def check_egress_acls(acls, dst_ip):
                for acl in acls:
                    # Check ipv4 acl rule only
                    if acl.get("cidr_block"):
                        # Check IP
                        if dst_ip in ip_network(acl["cidr_block"], strict=False):
                            # Check Port
                            if (acl.get("protocol") == "-1") or (
                                src_port_from
                                and src_port_to
                                and set(range(src_port_from, src_port_to)).issubset(
                                    range(
                                        acl["port_range"]["from"],
                                        acl["port_range"]["to"] + 1,
                                    )
                                )
                            ):
                                # Check Action
                                if acl["rule_action"] == "allow":
                                    return True
                                else:
                                    self.fail_json(
                                        msg=f"Destination Subnet Network Acl Egress Rules do not allow outbound traffic to source: {self.src_ip}"
                                    )
                else:
                    self.fail_json(
                        msg=f"Destination Subnet Network Acl Egress Rules do not allow outbound traffic to source: {self.src_ip}"
                    )

            def check_ingress_acls(acls, src_ip, dst_port):
                for acl in acls:
                    # Check ipv4 acl rule only
                    if acl.get("cidr_block"):
                        # Check IP
                        if src_ip in ip_network(acl["cidr_block"], strict=False):
                            # Check Port
                            if (acl.get("protocol") == "-1") or (
                                dst_port
                                in range(
                                    acl["port_range"]["from"],
                                    acl["port_range"]["to"] + 1,
                                )
                            ):
                                # Check Action
                                if acl["rule_action"] == "allow":
                                    return True
                                else:
                                    self.fail_json(
                                        msg=f"Destination Subnet Network Acl Ingress Rules do not allow inbound traffic from source: {self.src_ip} towards destination port {str(self.dst_port)}"
                                    )
                else:
                    self.fail_json(
                        msg=f"Destination Subnet Network Acl Ingress Rules do not allow inbound traffic from source: {self.src_ip} towards destination port {str(self.dst_port)}"
                    )

            egress_acls = [acl for acl in acls["nacls"] if acl["egress"]]
            ingress_acls = [acl for acl in acls["nacls"] if not acl["egress"]]

            dst_ingress_check_pass = check_ingress_acls(ingress_acls, src_ip, dst_port)
            dst_egress_check_pass = check_egress_acls(egress_acls, src_ip)

            if dst_ingress_check_pass and dst_egress_check_pass:
                return True

        eval_src_nacls(self.src_network_acls)
        eval_dst_nacls(self.dts_network_acls)

        return True

    def execute_module(self):
        try:
            # Evaluate Ingress and Egress network ACLs
            self.eval_nacls()
            self.exit_json(result="Network ACLs evaluation successful")
        except Exception as e:
            self.fail_json(
                msg="Network ACLs evaluation failed: {}".format(e), exception=e
            )


def main():

    EvalNetworkAcls()


if __name__ == "__main__":
    main()
