#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: validate_network_acls
short_description: Evaluates network ACLs
author:
  - Aubin Bikouo (@abikouo)
description:
  - Compare the Source to Destination network ACLs.
  - Source can be an EC2 instance trying to connect to an RDS instance (Destination).

options:
  dest_subnet_cidrs:
    description:
    - Destination Subnet CIDRs.
    type: list
    elements: str
    required: true
  dest_network_acl_rules:
    description:
    - Destination Network ACL Rules.
    type: list
    elements: dict
    required: true
  dest_port:
    description:
    - Destination Endpoint Ports.
    type: list
    elements: int
    required: true
  src_network_acl_rules:
    description:
    - Source Network ACL Rules.
    type: list
    elements: dict
    required: true
  src_private_ip:
    description:
    - Source Private IP.
    type: list
    elememts: str
    required: true

"""

EXAMPLES = r"""
- name: Evaluate network ACLS from EC2 instance to RDS Instance
  cloud.aws_ops.validate_network_acls:
    dest_subnet_cidrs:
        - 10.1.0.0/24
        - 10.1.2.0/24
    dest_network_acl_rules:
        - egress:
            - [100, "all", "allow", "0.0.0.0/0", null, null, 0, 65535]
          ingress:
            - [100, "all", "allow", "0.0.0.0/0", null, null, 0, 65535]
          is_default: true
          nacl_id: "acl-01124846ef9f50ff2"
          owner_id: "000000000000"
          subnets:
            - "subnet-0af56e0d353f88cb8"
            - "subnet-032f1a2598b6318ed"]
          vpc_id: "vpc-0274c44deffd7368a
    dest_port:
        - 5432
    src_network_acl_rules:
        - egress:
            - [100, "all", "allow", "0.0.0.0/0", null, null, 0, 65535]
          ingress:
            - [100, "all", "allow", "0.0.0.0/0", null, null, 0, 65535]
          is_default: true
          nacl_id: "acl-01124846ef9f50ff2"
          owner_id: "000000000000"
          subnets:
            - subnet-0af56e0d353f88cb8
            - subnet-032f1a2598b6318ed
          vpc_id: "vpc-0274c44deffd7368a"
    src_private_ip:
        - 172.10.3.10

"""

RETURN = r"""
result:
  type: str
  description: Results from comparing the Source network ACLs to the Destination network ACLs.
  returned: success
  sample: 'Network ACL validation successful'
"""

from ipaddress import ip_network, ip_address
from collections import namedtuple
from ansible.module_utils.basic import AnsibleModule


# NACL Entry format
# [
#   100,            -> Rule number
#   "all",          -> protocol
#   "allow",        -> Rule action
#   "0.0.0.0/0",    -> CIDR block
#   null,           -> icmp type
#   null,           -> icmp code
#   0,              -> port range from
#   65535           -> port range to
# ]
NACLEntry = namedtuple(
    "NACLEntry",
    [
        "rule_number",
        "protocol",
        "rule_action",
        "cidr_block",
        "icmp_type",
        "icmp_code",
        "port_range_from",
        "port_range_to",
    ],
)


def is_port_in_range(port, from_port, to_port):
    if from_port is not None and to_port is not None:
        return port in range(from_port, to_port + 1)
    return True


class ValidateNetworkACL(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            dest_subnet_cidrs=dict(type="list", elements="str", required=True),
            dest_network_acl_rules=dict(type="list", elements="dict", required=True),
            dest_port=dict(type="list", elements="int", required=True),
            src_network_acl_rules=dict(type="list", elements="dict", required=True),
            src_private_ip=dict(type="list", elements="str", required=True),
        )

        super(ValidateNetworkACL, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def evaluate_network_traffic(self, acl, egress=True):
        allowed_ports = []
        denied_ports = []

        for port in self.dest_port:
            if port in allowed_ports or port in denied_ports:
                continue
            acl_entries = acl.get("egress", []) if egress else acl.get("ingress", [])
            for entry in acl_entries:
                nacl_entry = NACLEntry(*entry)

                if egress:
                    # Evaluate traffic based on CIDR when egress is set to True
                    eval_traffic = (
                        ip_network(nacl_entry.cidr_block, strict=False).overlaps(
                            ip_network(cidr, strict=False)
                        )
                        for cidr in self.dest_subnet_cidrs
                    )
                else:
                    # Evaluate traffic based on IP when egress is set to False
                    eval_traffic = (
                        ip_address(ip)
                        in ip_network(nacl_entry.cidr_block, strict=False)
                        for ip in self.src_private_ip
                    )

                if (
                    nacl_entry.protocol in ("all", "tcp")
                    and is_port_in_range(
                        port, nacl_entry.port_range_from, nacl_entry.port_range_to
                    )
                    and any(eval_traffic)
                ):
                    if nacl_entry.rule_action == "allow":
                        allowed_ports.append(port)
                    else:
                        denied_ports.append(port)

        if len(denied_ports) > 0:
            acl_type = "egress" if egress else "ingress"
            self.fail_json(
                msg="Network acl {id} is not allowing traffic for port(s) {ports}."
                "Please review network acl for {acl_type} rules allowing port(s) {ports}".format(
                    id=acl.get("nacl_id"),
                    ports=denied_ports,
                    acl_type=acl_type,
                )
            )

    def execute_module(self):
        try:
            # Verify Egress traffic from Source to Destination subnets
            for acl in self.src_network_acl_rules:
                self.evaluate_network_traffic(acl, egress=True)

            # Verify Ingress traffic to Destination from Source Instance IP
            for acl in self.dest_network_acl_rules:
                self.evaluate_network_traffic(acl, egress=False)

            self.exit_json(result="Network ACL validation successful")

        except Exception as e:
            self.fail_json(
                msg="Network ACL validation failed: {}".format(e), exception=e
            )


def main():

    ValidateNetworkACL()


if __name__ == "__main__":
    main()
