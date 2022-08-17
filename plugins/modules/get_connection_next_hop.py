#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: get_connection_next_hop
short_description: Get connection next hop type
description:
  - Get connection next hop type.
author:
  - Alina Buzachis (@alinabuzachis)
options:
  dst_ip:
    description:
    - The IPv4 address of the resource you want to connect to.
    type: str
    required: true
  routes:
    description:
    - VPC route tables.
    type: list
    elements: dict
    required: true
"""


EXAMPLES = r"""
- name: Get connection next hop type
  get_connection_next_hop:
    ...

"""


RETURN = r"""
result:
  type: str
  description: Results from get connection next hop type.
  returned: success
  sample: 'local'
"""


from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class GetConnectionNextHopType(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            dst_ip=dict(type="str", required=True),
            routes=dict(type="list", elements="str", required=True),
        )

        super(GetConnectionNextHopType, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def get_next_hop(self):
        destination = ip_address(self.dst_ip)
        most_specific = -1

        for route in self.routes:
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
        if most_specific >= 0:
            return (
                next_hop.get("egress_only_internet_gateway_id")
                or next_hop.get("gateway_id")
                or next_hop.get("instance_id")
                or next_hop.get("network_interface_id")
                or next_hop.get("local_gateway_id")
                or next_hop.get("nat_gateway_id")
                or next_hop.get("transit_gateway_id")
                or next_hop.get("vpc_peering_connection_id")
            )
        self.fail_json(msg=f"No route found for destination: {self.dst_ip}")

    def execute_module(self):
        next_hop = None

        try:
            next_hop = self.get_next_hop()
            self.exit_json(next_hoop=next_hop)
        except Exception as e:
            self.fail_json(
                msg="Failed to get connection next hop type: {}".format(e), exception=e
            )


def main():

    GetConnectionNextHopType()


if __name__ == "__main__":
    main()
