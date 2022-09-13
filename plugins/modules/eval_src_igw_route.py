#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: eval_src_igw_route
short_description: Evaluate source IP, security groups and network ACLs
description:
  - Evaluate source IP, security groups and network ACLs.
  - Confirms whether the source has a public IP address associated with the resource, if the route destination is an internet gateway.
  - Confirms whether the security group rules allow the needed traffic from the source to the destination resource.
  - Confirms whether the network ACLs allow the needed traffic from the source resource.
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
  src_network_interface:
    description:
    - Soure network interface information.
    type: dict
    required: true
  src_security_groups_info:
    description:
    - Source security groups information.
    type: list
    elements: dict
    required: true
  src_network_acls:
    description:
    - Source subnet network ACLs rules.
    type: list
    elements: dict
    required: true
"""


EXAMPLES = r"""
- name: Evaluate ingress and egress network ACLs
  eval_src_igw_route:
    src_ip: "192.168.0.112
    src_subnet_id: "subnet-03181dc286eca1244"
    dst_ip: "8.8.8.8"
    dst_port: 80
    # Network ACL entries order
    # ["rule_number", "protocol", "rule_action", "cidr_block", "icmp_type", "icmp_code", "port_from", "port_to"]
    src_network_acls:
        - egress:
            - - 100
              - "all"
              - "allow"
              - "0.0.0.0/0"
              - null
              - null
              - 0
              - 65535
        - ingress:
            - - 100
              - "all"
              - "allow"
              - "0.0.0.0/0"
              - null
              - null
              - 0
              - 65535
    src_network_interface:
        association:
            ip_owner_id: "amazon"
            public_dns_name: "ec2-3-93-192-138.compute-1.amazonaws.com"
            public_ip: "3.93.192.138"
        attachment:
            attach_time: "2022-08-29T12:49:23+00:00"
            attachment_id: "eni-attach-01c6b11b7ea6d15da"
            delete_on_termination: true
            device_index: 0
            instance_id: "i-093745484bef0531c"
            instance_owner_id: "721066863947"
            network_card_index: 0
            status: "attached"
        availability_zone: "us-east-1a"
        description: ""
        groups:
            - group_id: "sg-030921b67798a88fd"
              group_name: "sg_ansibleVPC_publicsubnet_jumphost"
        id: "eni-046bc4b5d5249b832
        interface_type: "interface
        ipv6_addresses: []
        mac_address: "0e:32:64:a5:39:f7"
        network_interface_id: "eni-046bc4b5d5249b832"
        owner_id: "721066863947"
        private_dns_name: "ip-192-168-0-11.ec2.internal"
        private_ip_address: "192.168.0.11"
        private_ip_addresses:
            - association":
                ip_owner_id: "amazon"
                public_dns_name: "ec2-3-93-192-138.compute-1.amazonaws.com"
                public_ip: "3.93.192.138"
              primary: true
              private_dns_name: "ip-192-168-0-11.ec2.internal"
              private_ip_address: "192.168.0.11"
        requester_managed: false
        source_dest_check: true
        status: "in-use"
        subnet_id: "subnet-03181dc286eca1244"
        tag_set: {}
        tags: {}
        vpc_id: "vpc-02c18b2cb55d28ff3"
    src_port_range: null
    src_security_groups_info:
        - description: "Allow 22 and 80 ports open"
          group_id: "sg-0258afe8541042bac"
          group_name: "sg_ansibleVPC_publicsubnet_jumphost"
          ip_permissions:
            - from_port: 80
              ip_protocol: "tcp"
              ip_ranges:
                - cidr_ip: "223.230.126.232/32"
                  description: "Allow 22 and 80 from all"
              ipv6_ranges: []
              prefix_list_ids: []
              to_port: 80
              user_id_group_pairs: []
            - from_port: 22
              ip_protocol: "tcp"
              ip_ranges:
                - cidr_ip: "192.168.0.0/24"
                - cidr_ip: "223.230.126.232/32"
                  description: "Allow 22 and 80 from all"
              ipv6_ranges: []
              prefix_list_ids: []
              to_port: 22
              user_id_group_pairs: []
          ip_permissions_egress:
            - ip_protocol: "-1"
              ip_ranges":
                - cidr_ip: "0.0.0.0/0"
              ipv6_ranges: [],
              prefix_list_ids: []
              user_id_group_pairs: []
          owner_id: "721066863947"
          tags: {}
          vpc_id: "vpc-097bb89457aa6d8f3"
"""


RETURN = r"""
result:
  type: str
  description: Results from evaluating source IP, security groups and network ACLs.
  returned: success
  sample: 'Source evaluation successful'
"""


from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class EvalSrcIgwRoute(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            src_ip=dict(type="str", required=True),
            src_network_interface=dict(type="dict", required=True),
            src_port_range=dict(type="str", required=False),
            dst_ip=dict(type="str", required=True),
            dst_port=dict(type="str", required=True),
            src_subnet_id=dict(type="str", required=True),
            src_security_groups_info=dict(type="list", elements="dict", required=True),
            src_network_acls=dict(type="list", elements="dict", required=True),
        )

        super(EvalSrcIgwRoute, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def eval_src_public_ip(self):
        private_ips = self.src_network_interface["private_ip_addresses"]

        for private_ip in private_ips:
            if private_ip["private_ip_address"] == self.src_ip:
                if "public_ip" in str(private_ip):
                    return True

        self.fail_json(
            msg="A public IP or Elastic IP is required at source to connect to a public destination"
        )

    def eval_src_egress_rule(self):
        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)

        for sg in self.src_security_groups_info:
            for rule in sg["ip_permissions_egress"]:
                if (
                    (rule.get("ip_protocol") == "-1")
                    or (rule.get("from_port") == -1 and rule.get("to_port") == -1)
                    or (
                        dst_port
                        in range(rule.get("from_port"), rule.get("to_port") + 1)
                    )
                ):
                    for cidr in rule["ip_ranges"]:
                        if dst_ip in ip_network(cidr["cidr_ip"], strict=False):
                            return True
        self.fail_json(
            msg=f"Egress rules on source do not allow traffic towards destination: {self.dst_ip} : {str(dst_port)}"
        )

    def eval_src_nacls(self):
        def check_egress_acls(acls, dst_ip, dst_port):
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
                                    msg=f"Source Subnet {self.src_subnet_id} Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(self.dst_port)}"
                                )
            else:
                self.fail_json(
                    msg=f"Source Subnet {self.src_subnet_id} Network Acl Egress Rules do not allow outbound traffic to destination: {self.dst_ip} : {str(self.dst_port)}"
                )

        def check_ingress_acls(acls, src_ip):

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
                                    msg=f"Source Subnet {self.src_subnet_id} Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                                )
            else:
                self.fail_json(
                    msg=f"Source Subnet {self.src_subnet_id} Network Acl Ingress Rules do not allow inbound traffic from destination: {self.dst_ip}"
                )

        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)
        src_port_from = None
        src_port_to = None
        if self.src_port_range:
            src_port_from = int(self.src_port_range.split("-")[0])
            src_port_to = int(self.src_port_range.split("-")[1])
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

        egress_acls = [acl["egress"] for acl in self.src_network_acls if acl["egress"]][
            0
        ]
        ingress_acls = [
            acl["ingress"] for acl in self.src_network_acls if acl["ingress"]
        ][0]

        src_egress_check_pass = check_egress_acls(egress_acls, dst_ip, dst_port)
        src_ingress_check_pass = check_ingress_acls(ingress_acls, dst_ip)

        if src_ingress_check_pass and src_egress_check_pass:
            return True

        self.fail_json(msg="Network ACLs do not allow traffic")

    def execute_module(self):
        try:
            self.eval_src_public_ip()
            self.eval_src_egress_rule()
            self.eval_src_nacls()
            self.exit_json(result="Source evaluation successful")
        except Exception as e:
            self.fail_json(msg="Source evaluation failed: {}".format(e), exception=e)


def main():

    EvalSrcIgwRoute()


if __name__ == "__main__":
    main()
