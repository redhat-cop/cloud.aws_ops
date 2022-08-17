#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: eval_security_groups
short_description: Evaluate ingress and egress security group rules
description:
  - Evaluates ingress and egress security group rules.
author:
  - Alina Buzachis (@alinabuzachis)
options:
  src_ip:
    description:
    - The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
    type: str
    required: true
  src_security_groups:
    description:
    - Destination Security Groups.
    type: list
    elements: list
    required: true
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
  dst_security_groups:
    description:
    - Destination Security Groups.
    type: list
    elements: str
    required: true
  security_groups:
    description:
    - Security Groups.
    type: list
    elements: dict
    required: true
"""


EXAMPLES = r"""
- name: Evaluate ingress and egress security group rules
  eval_security_groups:
    ...

"""


RETURN = r"""
result:
  type: str
  description: Results from evaluating ingress and egress security group rules.
  returned: success
  sample: 'Security Groups rules evaluation successful'
"""


from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class EvalSecurityGroups(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            src_ip=dict(type="str", required=True),
            src_security_groups=dict(type="list", elements="str", required=True),
            dst_ip=dict(type="str", required=True),
            dst_port=dict(type="str", required=True),
            dst_security_groups=dict(type="list", elements="str", required=True),
            security_groups=dict(type="list", elements="dict", required=True),
        )

        super(EvalSecurityGroups, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def eval_sg_rules(self):
        src_ip = ip_address(self.src_ip)
        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)

        def eval_src_egress_rules():
            for src_security_group in self.src_security_groups:
                sg = [
                    group
                    for group in self.security_groups["security_groups"]
                    if group["group_id"] == src_security_group
                ][0]
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
                        else:
                            for group in rule["user_id_group_pairs"]:
                                if any(
                                    sg in group["group_id"]
                                    for sg in self.dst_security_groups
                                ):
                                    return True
            self.fail_json(
                msg=f"Egress rules on source do not allow traffic towards destination: {self.dst_ip} : {str(dst_port)}"
            )

        def eval_dst_ingress_rules():
            for dst_security_group in self.dst_security_groups:
                sg = [
                    group
                    for group in self.security_groups["security_groups"]
                    if group["group_id"] == dst_security_group
                ][0]
                for rule in sg["ip_permissions"]:
                    if (
                        (rule.get("ip_protocol") == "-1")
                        or (rule.get("from_port") == -1 and rule.get("to_port") == -1)
                        or (
                            dst_port
                            in range(rule.get("from_port"), rule.get("to_port") + 1)
                        )
                    ):
                        for cidr in rule["ip_ranges"]:
                            if src_ip in ip_network(cidr["cidr_ip"], strict=False):
                                return True
                        else:
                            for group in rule["user_id_group_pairs"]:
                                if any(
                                    sg in group["group_id"]
                                    for sg in self.src_security_groups
                                ):
                                    return True
            self.fail_json(
                msg=f"Ingress rules on destination do not allow traffic from source: {self.src_ip} towards destination port {str(dst_port)}"
            )

        eval_src_egress_rules()
        eval_dst_ingress_rules()

        return True

    def check_src_egress_rules(self):
        dst_ip = ip_address(self.dst_ip)
        dst_port = int(self.dst_port)

        for sg in self.src_security_groups:
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
            msg="Egress rules on source do not allow traffic towards destination: "
            + self.dst_ip
            + ":"
            + str(dst_port)
        )

    def execute_module(self):
        try:
            # Evluate Ingress and Egress security groups rules
            self.check_src_egress_rules()
            self.eval_sg_rules()
            self.exit_json(result="Security Groups rules validation successful")
        except Exception as e:
            self.fail_json(
                msg="Security Groups rules validation failed: {}".format(e), exception=e
            )


def main():

    EvalSecurityGroups()


if __name__ == "__main__":
    main()
