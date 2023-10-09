#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: validate_security_group_rules
short_description: Evaluates Security group Rules
author:
  - Aubin Bikouo (@abikouo)
description:
  - Compare the Source to Destination Security group Rules.
  - Source can be an EC2 instance trying to connect to an RDS instance (Destination).

options:
  dest_subnet_cidrs:
    description:
    - Destination Subnets CIDRs.
    type: list
    elements: str
    required: true
  dest_security_groups:
    description:
    - Destination Security Groups Rules.
    type: list
    elements: dict
    required: true
  dest_port:
    description:
    - Destination Endpoint Port.
    type: int
    required: true
  protocol:
    description:
    - Protocol to evaluate Security Group.
    type: str
    default: tcp
  src_security_groups:
    description:
    - Source Security Groups Rules.
    type: list
    elements: dict
    required: true
  src_private_ip:
    description:
    - Source Private IP.
    type: str
    required: true

"""

EXAMPLES = r"""
- name: Evaluate Security group rules from EC2 instance to RDS Instance
  cloud.aws_ops.validate_security_group_rules:
    dest_subnet_cidrs:
      - 10.1.0.0/24
      - 10.1.2.0/24
    dest_security_groups:
      - description: "Security group for EC2 instance"
        group_id: "sg-0bd2d9a14af754812"
        group_name: "aubin-sg"
        ip_permissions:
          - from_port: 5432
            to_port: 5432
            ip_protocol: "tcp"
            ip_ranges:
              - cidr_ip: "0.0.0.0/0"
            ipv6_ranges: []
            prefix_list_ids: []
            user_id_group_pairs: []
        ip_permissions_egress:
          - ip_protocol: -1
            ip_ranges:
              - cidr_ip: "0.0.0.0/0"
            ipv6_ranges: []
            prefix_list_ids: []
            user_id_group_pairs: []
        owner_id: "0000000000000"
        vpc_id: "vpc-0bee28efef41e1de4"
    dest_port: 5432
    src_security_groups:
      - description: "Security group for EC2 instance"
        group_id: "sg-0bd2d9a14af8a8998"
        group_name: "aubin-sg"
        ip_permissions:
          - from_port: 22
            to_port: 22
            ip_protocol: "tcp"
            ip_ranges:
              - cidr_ip: "0.0.0.0/0"
            ipv6_ranges: []
            prefix_list_ids: []
            user_id_group_pairs: []
        ip_permissions_egress:
          - ip_protocol: -1
            ip_ranges:
              - cidr_ip: "0.0.0.0/0"
            ipv6_ranges: []
            prefix_list_ids: []
            user_id_group_pairs: []
        owner_id: "0000000000000"
        vpc_id: "vpc-0bee28efef41e1de4"
    src_private_ip: "172.10.3.10"
"""

RETURN = r"""
result:
  type: str
  description: Results from comparing the Source security group rules to the Destination security group rules.
  returned: success
  sample: 'Security Group validation successful'
"""

from ipaddress import ip_network, ip_address
import copy

from ansible.module_utils.basic import AnsibleModule


class ValidateSecurityGroupRules(AnsibleModule):
    def __init__(self):
        argument_spec = dict(
            dest_subnet_cidrs=dict(type="list", elements="str", required=True),
            dest_security_groups=dict(type="list", elements="dict", required=True),
            dest_port=dict(type="int", required=True),
            src_security_groups=dict(type="list", elements="dict", required=True),
            src_private_ip=dict(type="str", required=True),
            protocol=dict(type="str", default="tcp"),
        )

        super(ValidateSecurityGroupRules, self).__init__(argument_spec=argument_spec)

        self.execute_module()

    def evaluate_security_group_rules_basedon_cidr(
        self, security_group, security_group_ids
    ):
        remote_cidrs = self.params.get("dest_subnet_cidrs")
        required_cidrs = copy.deepcopy(remote_cidrs)
        dest_port = self.params.get("dest_port")
        protocol = self.params.get("protocol")
        for rule in security_group.get("ip_permissions_egress", []):
            if (
                rule["ip_protocol"] == protocol
                and dest_port in range(rule["from_port"], rule["to_port"] + 1)
            ) or (rule["ip_protocol"] == "-1"):
                for group in rule["user_id_group_pairs"]:
                    if group["group_id"] in security_group_ids:
                        return
                for remote_cidr in remote_cidrs:
                    for cidrs in rule["ip_ranges"]:
                        if ip_network(cidrs["cidr_ip"], strict=False).overlaps(
                            ip_network(remote_cidr, strict=False)
                        ):
                            required_cidrs.remove(remote_cidr)
                            break

        if len(required_cidrs) > 0:
            return "Security group {id} is not allowing {protocol} traffic to/from IP ranges {ip_addr} for port(s) {port}.".format(
                id=security_group.get("group_id"),
                ip_addr=required_cidrs,
                port=dest_port,
                protocol=protocol,
            )

    def evaluate_security_group_rules_basedon_ip(
        self, security_group, security_group_ids
    ):
        for rule in security_group.get("ip_permissions", []):
            if (
                rule["ip_protocol"] == self.params.get("protocol")
                and self.params.get("dest_port")
                in range(rule["from_port"], rule["to_port"] + 1)
            ) or (rule["ip_protocol"] == "-1"):
                for group in rule["user_id_group_pairs"]:
                    if group["group_id"] in security_group_ids:
                        return
                for cidrs in rule["ip_ranges"]:
                    if ip_address(self.params.get("src_private_ip")) in ip_network(
                        cidrs["cidr_ip"], strict=False
                    ):
                        return

        return "Security group {id} is not allowing {protocol} traffic to/from IP {ip_addr} for port(s) {port}.".format(
            id=security_group.get("group_id"),
            protocol=self.params.get("protocol"),
            ip_addr=self.params.get("src_private_ip"),
            port=self.params.get("dest_port"),
        )

    def execute_module(self):
        try:
            dest_secgroup_ids = [
                x["group_id"] for x in self.params.get("dest_security_groups")
            ]
            src_secgroup_ids = [
                x["group_id"] for x in self.params.get("src_security_groups")
            ]

            # Verify Egress traffic from Source Instance to Destination subnets
            result = None
            for sec_group in self.params.get("src_security_groups"):
                result = self.evaluate_security_group_rules_basedon_cidr(
                    sec_group, dest_secgroup_ids
                )
                if result is None:
                    break

            if result:
                self.fail_json(
                    msg="{msg}. Please review security group(s) {ids} for rules allowing egress TCP traffic to port {port}".format(
                        msg=result,
                        ids=src_secgroup_ids,
                        port=self.params.get("dest_port"),
                    )
                )

            # Verify Ingress traffic to Destination from Source Instance IP
            for sec_group in self.params.get("dest_security_groups"):
                result = self.evaluate_security_group_rules_basedon_ip(
                    sec_group, src_secgroup_ids
                )
                if result is None:
                    break

            if result:
                self.fail_json(
                    msg="{msg}.Please review security group(s) {ids} for rules allowing ingress TCP traffic from port {port}".format(
                        msg=result,
                        ids=dest_secgroup_ids,
                        port=self.params.get("dest_port"),
                    )
                )

            self.exit_json(result="Security Group validation successful")

        except Exception as e:
            self.fail_json(
                msg="Security Group validation failed: {0}".format(e), exception=e
            )


def main():
    ValidateSecurityGroupRules()


if __name__ == "__main__":
    main()
