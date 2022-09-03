#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: eval_vpc_peering
short_description: Evaluate VPC peering connection between Source and Destination
description:
    - Evaluate VPC peering connection between Source and Destination.
    - Confirms both VPCs are in the same Region and that the id returned for the destination VPC matches the value specified.
    - Confirms whether the peered VPC has a route to the peering connection.
author:
    - Alina Buzachis (@alinabuzachis)
options:
    src_ip:
        description:
        - The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
        type: str
        required: true
    dst_vpc:
        description:
        - The ID of the Amazon VPC you want to test connectivity to.
        type: str
        required: false
    dst_peering_id:
        description:
        - The ID of the Destination Peering Connection.
        type: str
        required: true
    vpc_peering_connection:
        description:
        - Destination Peering Connection information.
        type: dict
        required: true
    routes:
        description:
        - VPC peering routes.
        type: list
        elements: dict
        required: true
"""


EXAMPLES = r"""
- name: Evaluate VPC peering
  eval_vpc_peering:
    src_ip: "172.25.0.9"
    dst_vpc: "vpc-09620d5e5c8622e06"
    peering_id: "pcx-054dfaa54c74adba4"
    vpc_peering_connection:
        accepter_vpc_info:
            cidr_block: "172.25.0.0/28"
            cidr_block_set:
                - cidr_block: "172.25.0.0/28"
            owner_id": "721066863947"
            peering_options:
                allow_dns_resolution_from_remote_vpc: false
                allow_egress_from_local_classic_link_to_remote_vpc: false
                allow_egress_from_local_vpc_to_remote_classic_link: false
            region: "us-east-1"
            vpc_id: "vpc-0e50f118140008d0c"
        requester_vpc_info:
            cidr_block: "173.24.0.0/28"
            cidr_block_set:
                - cidr_block": "173.24.0.0/28"
            owner_id: "721066863947"
            peering_options:
                allow_dns_resolution_from_remote_vpc: false
                allow_egress_from_local_classic_link_to_remote_vpc: false
                allow_egress_from_local_vpc_to_remote_classic_link: false
            region: "us-east-1"
            vpc_id": "vpc-09620d5e5c8622e06"
        status:
            code: "active"
            message: "Active"
        tags: {}
        vpc_peering_connection_id: "pcx-054dfaa54c74adba4"
    routes:
        - destination_cidr_block: "172.25.0.0/28"
          gateway_id: null
          instance_id: null,
          interface_id: null
          network_interface_id: null
          origin: "CreateRoute"
          state: "active"
          vpc_peering_connection_id: "pcx-054dfaa54c74adba4"
        - destination_cidr_block: "173.24.0.0/28"
          gateway_id: "local"
          instance_id: null
          interface_id: null
          network_interface_id": null
          origin: "CreateRouteTable"
          state: "active"
"""


RETURN = r"""
result:
    type: str
    description: Results from evaluating VPC peering.
    returned: success
    sample: 'VPC peering evaluation successful'
"""


from ipaddress import ip_network, ip_address
from ansible.module_utils.basic import AnsibleModule


class EvalVpcPeering(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            src_ip=dict(type="str", required=True),
            dst_vpc=dict(type="str", required=False),
            peering_id=dict(type="str", required=True),
            routes=dict(type="list", elements="dict", required=True),
            vpc_peering_connection=dict(type="dict", required=True),
        )

        super(EvalVpcPeering, self).__init__(argument_spec=argument_spec)

        for key in argument_spec:
            setattr(self, key, self.params.get(key))

        self.execute_module()

    def check_vpc_peering_connection(self):
        if (
            self.vpc_peering_connection["accepter_vpc_info"]["region"]
            == self.vpc_peering_connection["requester_vpc_info"]["region"]
        ):
            pass
        else:
            self.fail_json(
                msg="Troubleshooting Cross Region peering connection is not yet supported"
            )
        if self.dst_vpc and self.dst_vpc != "":
            if self.dst_vpc in str(self.peering_info):
                pass
            else:
                self.fail_json(
                    msg="Kindly check the VPC peering route in route table at the source resource subnet, it does not match the expected destination VPC"
                )

        return True

    def eval_peer_route_table(self):
        src_ip = ip_address(self.src_ip)
        most_specific = -1
        next_hop = {}

        for route in self.routes:
            if route.get("destination_cidr_block"):
                mask = int(route["destination_cidr_block"].split("/")[1])
                if (
                    "destination_prefix_list_id" not in str(route)
                    and src_ip
                    in ip_network(route["destination_cidr_block"], strict=False)
                    and mask > most_specific
                ):
                    if route["state"] != "blackhole":
                        most_specific = mask
                        next_hop = route
        if next_hop.get("vpc_peering_connection_id") == self.peering_id:
            return True
        else:
            self.fail_json(
                msg=f"Destination Subnet route table does not contain a valid peering route for source: {self.scr_ip}"
            )

    def execute_module(self):
        try:
            self.check_vpc_peering_connection()
            self.eval_peer_route_table()
            self.exit_json(result="VPC peering evaluation successful")
        except Exception as e:
            self.fail_json(
                msg="VPC peering evaluation failed: {}".format(e), exception=e
            )


def main():

    EvalVpcPeering()


if __name__ == "__main__":
    main()
