#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: validate_route_tables
short_description: Evaluates Route tables
author:
  - Aubin Bikouo (@abikouo)
description:
  - Compare the Source to Destination routes.
  - Source can be an EC2 instance trying to connect to an RDS instance (Destination).

options:
  dest_subnets:
    description:
    - Destination Subnet.
    type: list
    elements: dict
    required: true
  dest_route_tables:
    description:
    - Destination Route Tables.
    type: list
    elements: dict
    required: true
  dest_vpc_route_tables:
    description:
    - Destination Route Tables.
    type: list
    elements: dict
    required: true
  src_subnets:
    description:
    - Source Subnets.
    type: list
    elements: dict
    required: true
  src_private_ip:
    description:
    - Source Private IPs.
    type: list
    elements: str
    required: true
  src_route_tables:
    description:
    - Source Route Tables.
    type: list
    elements: dict
    required: true
  src_vpc_route_tables:
    description:
    - Source Route Tables.
    type: list
    elements: dict
    required: true

"""

EXAMPLES = r"""
- name: Evaluate routes from EC2 instance to RDS Instance
  cloud.aws_ops.validate_route_tables:
    dest_subnets:
        - assign_ipv6_address_on_creation: false
          availability_zone: "eu-west-2b"
          availability_zone_id: "euw2-az3"
          available_ip_address_count: 250
          cidr_block: "172.10.2.0/24"
          default_for_az: false
          enable_dns64: false
          id: "subnet-032f1a2598b6318ed"
          ipv6_cidr_block_association_set: []
          ipv6_native: false
          map_customer_owned_ip_on_launch: false
          map_public_ip_on_launch: false
          owner_id: "00000000000"
          private_dns_name_options_on_launch:
            enable_resource_name_dns_a_record: false
            enable_resource_name_dns_aaaa_record: false
            hostname_type: "ip-name"
          state: "available"
          subnet_arn: "arn:aws:ec2:eu-west-2:721066863947:subnet/subnet-032f1a2598b6318ed"
          subnet_id: "subnet-032f1a2598b6318ed"
          vpc_id: "vpc-0274c44deffd7368a"
        - assign_ipv6_address_on_creation: false
          availability_zone: "eu-west-2a"
          availability_zone_id: "euw2-az2"
          available_ip_address_count: 250
          cidr_block: "172.10.1.0/24"
          default_for_az: false
          enable_dns64: false
          id: "subnet-0af56e0d353f88cb8"
          ipv6_cidr_block_association_set: []
          ipv6_native: false
          map_customer_owned_ip_on_launch: false
          map_public_ip_on_launch: false
          owner_id: "00000000000"
          private_dns_name_options_on_launch:
            enable_resource_name_dns_a_record: false
            enable_resource_name_dns_aaaa_record: false
            hostname_type: "ip-name"
          state: "available"
          subnet_arn: "arn:aws:ec2:eu-west-2:721066863947:subnet/subnet-0af56e0d353f88cb8"
          subnet_id: "subnet-0af56e0d353f88cb8"
          vpc_id: "vpc-0274c44deffd7368a"
    dest_route_tables:
        - associations:
            - association_state:
                state: "associated"
              id: "rtbassoc-0c5c333773772843b"
              main: false
              route_table_association_id: "rtbassoc-0c5c333773772843b"
              route_table_id: "rtb-07a81d1afe14a009c"
              subnet_id: "subnet-0ab63680e1e0316e2"
          id: "rtb-07a81d1afe14a009c"
          owner_id: "721066863947"
          propagating_vgws: []
          route_table_id: "rtb-07a81d1afe14a009c"
          routes:
            - destination_cidr_block: "10.1.0.0/16"
              gateway_id: "local"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRouteTable"
              state: "active"
            - destination_cidr_block: "0.0.0.0/0"
              gateway_id: "igw-057753b539008784c"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRoute"
              state": "active"
          vpc_id: "vpc-0bee28efef41e1de4"
    dest_vpc_route_tables:
        - associations:
            - association_state:
                state: "associated"
              id: "rtbassoc-0c5c333773772843b"
              main: false
              route_table_association_id: "rtbassoc-0c5c333773772843b"
              route_table_id: "rtb-07a81d1afe14a009c"
              subnet_id: "subnet-0ab63680e1e0316e2"
          id: "rtb-07a81d1afe14a009c"
          owner_id: "721066863947"
          propagating_vgws: []
          route_table_id: "rtb-07a81d1afe14a009c"
          routes:
            - destination_cidr_block: "10.1.0.0/16"
              gateway_id: "local"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRouteTable"
              state: "active"
            - destination_cidr_block: "0.0.0.0/0"
              gateway_id: "igw-057753b539008784c"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRoute"
              state": "active"
          vpc_id: "vpc-0bee28efef41e1de4"
    src_subnets:
        - assign_ipv6_address_on_creation: false
          availability_zone: "eu-west-2a"
          availability_zone_id: "euw2-az2"
          available_ip_address_count: 250
          cidr_block: "172.10.1.0/24"
          default_for_az: false
          enable_dns64: false
          id: "subnet-0af56e0d353f88cb8"
          ipv6_cidr_block_association_set: []
          ipv6_native: false
          map_customer_owned_ip_on_launch: false
          map_public_ip_on_launch: false
          owner_id: "00000000000"
          private_dns_name_options_on_launch:
            enable_resource_name_dns_a_record: false
            enable_resource_name_dns_aaaa_record": false
            hostname_type: "ip-name"
          state: "available"
          subnet_arn: "arn:aws:ec2:eu-west-2:721066863947:subnet/subnet-0af56e0d353f88cb8"
          subnet_id: "subnet-0af56e0d353f88cb8"
          vpc_id: "vpc-0274c44deffd7368a"
    src_private_ip:
        - 172.0.1.4
    src_route_tables:
        - associations:
            - association_state:
                state: "associated"
              id: "rtbassoc-0c5c333773772843b"
              main: false
              route_table_association_id: "rtbassoc-0c5c333773772843b"
              route_table_id: "rtb-07a81d1afe14a009c"
              subnet_id: "subnet-0ab63680e1e0316e2"
          id: "rtb-07a81d1afe14a009c"
          owner_id: "721066863947"
          propagating_vgws: []
          route_table_id: "rtb-07a81d1afe14a009c"
          routes:
            - destination_cidr_block: "10.1.0.0/16"
              gateway_id: "local"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRouteTable"
              state: "active"
            - destination_cidr_block: "0.0.0.0/0"
              gateway_id: "igw-057753b539008784c"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRoute"
              state: "active"
          vpc_id: "vpc-0bee28efef41e1de4"
    src_vpc_route_tables
        - associations:
            - association_state:
                state: "associated"
              id: "rtbassoc-0c5c333773772843b"
              main: false
              route_table_association_id: "rtbassoc-0c5c333773772843b"
              route_table_id: "rtb-07a81d1afe14a009c"
              subnet_id: "subnet-0ab63680e1e0316e2"
          id: "rtb-07a81d1afe14a009c"
          owner_id: "721066863947"
          propagating_vgws: []
          route_table_id: "rtb-07a81d1afe14a009c"
          routes:
            - destination_cidr_block: "10.1.0.0/16"
              gateway_id: "local"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRouteTable"
              state: "active"
            - destination_cidr_block: "0.0.0.0/0"
              gateway_id: "igw-057753b539008784c"
              instance_id: null
              interface_id: null
              network_interface_id: null
              origin: "CreateRoute"
              state: "active"
          vpc_id: "vpc-0bee28efef41e1de4"

"""

RETURN = r"""
result:
  type: str
  description: Results from comparing the Source route table to the Destination routes.
  returned: success
  sample: 'Route table validation successful'
"""

from ipaddress import ip_network
import copy

from ansible.module_utils.basic import AnsibleModule


class ValidateRouteTables(AnsibleModule):
    def __init__(self):

        argument_spec = dict(
            dest_subnets=dict(type="list", elements="dict", required=True),
            dest_route_tables=dict(type="list", elements="dict", required=True),
            dest_vpc_route_tables=dict(type="list", elements="dict", required=True),
            src_subnets=dict(type="list", elements="dict", required=True),
            src_private_ip=dict(type="list", elements="str", required=True),
            src_route_tables=dict(type="list", elements="dict", required=True),
            src_vpc_route_tables=dict(type="list", elements="dict", required=True),
        )

        super(ValidateRouteTables, self).__init__(argument_spec=argument_spec)

        self.execute_module()

    def validate_vpc(self, src_vpc_id, src_private_ips, dest_vpc_id, dest_subnet_cidrs):
        # Check whether resources are in the same VPC. If not, Cidr cannot overlap
        if not (dest_vpc_id[0] == src_vpc_id[0]):
            for dest_cidr in dest_subnet_cidrs:
                for ip_addr in src_private_ips:
                    if ip_network(dest_cidr, strict=False).overlaps(
                        ip_network(ip_addr, strict=False)
                    ):
                        self.fail_json(
                            msg="Resources are located in different VPCs, however, Cidrs are overlapping."
                        )
        else:
            self.exit_json(result="Resources located in the same VPC.")

    def validate_route_tables(
        self,
        src_route_tables,
        b_check_vpc_rtb_ec2,
        dest_route_tables,
        b_check_vpc_rtb_rds,
    ):
        # Check whether resources are using the same route table
        for rtb in dest_route_tables:
            self.rds_rtb_list.append(rtb["route_table_id"])

        for rtb in src_route_tables:
            self.ec2_rtb_list.append(rtb["route_table_id"])

        if (
            (dest_route_tables == src_route_tables)
            and not b_check_vpc_rtb_ec2
            and not b_check_vpc_rtb_rds
        ):
            self.exit_json(
                result="Source and destination resources are using the same route table(s): {0}".format(
                    self.ec2_rtb_list
                )
            )

    def validate_route_connection(
        self,
        src_private_ips,
        dest_vpc_route_tables,
        dest_route_tables,
        b_check_vpc_rtb_rds,
    ):

        # Third verification: Check wheter route is through a peering connection
        # Verify whether Destination RTBs contains route to Source network
        for rtb in dest_route_tables:
            required_ips = copy.deepcopy(src_private_ips)
            for route in rtb["routes"]:
                if "vpc_peering_connection_id" not in route.keys():
                    continue
                if len(required_ips) == 0:
                    break
                for remote_ip in src_private_ips:
                    if ip_network(
                        route["destination_cidr_block"], strict=False
                    ).overlaps(ip_network(remote_ip, strict=False)):
                        required_ips.remove(remote_ip)
            if len(required_ips) == 0:
                self.rds_rtb_list.remove(rtb["route_table_id"])

        if b_check_vpc_rtb_rds:
            for rtb in dest_vpc_route_tables:
                required_ips = copy.deepcopy(src_private_ips)
                for route in rtb["routes"]:
                    if "vpc_peering_connection_id" not in route.keys():
                        continue
                    if len(required_ips) == 0:
                        break
                    for remote_ip in src_private_ips:
                        if ip_network(
                            route["destination_cidr_block"], strict=False
                        ).overlaps(ip_network(remote_ip, strict=False)):
                            if remote_ip in required_ips:
                                required_ips.remove(remote_ip)
                if len(required_ips) == 0:
                    self.rds_rtb_list.remove(rtb["route_table_id"])

    def validate_route_to_dest_on_source(
        self,
        src_route_tables,
        src_vpc_route_tables,
        dest_subnet_cidrs,
        b_check_vpc_rtb_ec2,
    ):

        # Verify whether Source RTB contains route to Destination network
        for rtb in src_route_tables:
            required_cidrs = copy.deepcopy(dest_subnet_cidrs)
            for route in rtb["routes"]:
                if "vpc_peering_connection_id" not in route.keys():
                    continue
                if len(required_cidrs) == 0:
                    break
                for remote_cidr in dest_subnet_cidrs:
                    if ip_network(
                        route["destination_cidr_block"], strict=False
                    ).overlaps(ip_network(remote_cidr, strict=False)):
                        if remote_cidr in required_cidrs:
                            required_cidrs.remove(remote_cidr)
            if len(required_cidrs) == 0:
                self.ec2_rtb_list.remove(rtb["route_table_id"])

        if b_check_vpc_rtb_ec2:
            for rtb in src_vpc_route_tables:
                required_ips = copy.deepcopy(dest_subnet_cidrs)
                for route in rtb["routes"]:
                    if "vpc_peering_connection_id" not in route.keys():
                        continue
                    if len(required_cidrs) == 0:
                        break
                    for remote_cidr in dest_subnet_cidrs:
                        if ip_network(
                            route["destination_cidr_block"], strict=False
                        ).overlaps(ip_network(remote_cidr, strict=False)):
                            required_cidrs.remove(remote_cidr)
                if len(required_ips) == 0:
                    self.ec2_rtb_list.remove(rtb["route_table_id"])

    def execute_module(self):
        try:
            # RDS Info
            dest_subnet_ids = [x.get("id") for x in self.params.get("dest_subnets")]
            dest_subnet_cidrs = [
                x.get("cidr_block") for x in self.params.get("dest_subnets")
            ]
            dest_route_tables = self.params.get("dest_route_tables")
            dest_vpc_route_tables = self.params.get("dest_vpc_route_tables")
            dest_vpc_id = list(
                set(x.get("vpc_id") for x in self.params.get("dest_subnets"))
            )

            # EC2 Instance Info
            src_subnet_ids = [x.get("id") for x in self.params.get("src_subnets")]
            src_private_ips = self.params.get("src_private_ip")
            src_route_tables = self.params.get("src_route_tables")
            src_vpc_route_tables = self.params.get("src_vpc_route_tables")
            src_vpc_id = list(
                set(x.get("vpc_id") for x in self.params.get("src_subnets"))
            )

            self.rds_rtb_list = []
            self.ec2_rtb_list = []
            b_check_vpc_rtb_rds = False
            b_check_vpc_rtb_ec2 = False

            rds_rtb_subnet_list = []  # All subnets that contain a valid rtb
            ec2_rtb_subnet_list = []

            # Initializing RouteTables
            for rtb in dest_route_tables:
                for assoc in rtb["associations"]:
                    if assoc["subnet_id"] in dest_subnet_ids:
                        rds_rtb_subnet_list.append(assoc["subnet_id"])
            if len(rds_rtb_subnet_list) < len(dest_subnet_ids):
                b_check_vpc_rtb_rds = True

            for rtb in src_route_tables:
                for assoc in rtb["associations"]:
                    if assoc["subnet_id"] in src_subnet_ids:
                        ec2_rtb_subnet_list.append(assoc["subnet_id"])
            if len(ec2_rtb_subnet_list) < len(src_subnet_ids):
                b_check_vpc_rtb_ec2 = True

            self.validate_vpc(
                src_vpc_id, src_private_ips, dest_vpc_id, dest_subnet_cidrs
            )
            self.validate_route_tables(
                src_route_tables,
                b_check_vpc_rtb_ec2,
                dest_route_tables,
                b_check_vpc_rtb_rds,
            )
            self.validate_route_connection(
                src_private_ips,
                dest_vpc_route_tables,
                dest_route_tables,
                b_check_vpc_rtb_rds,
            )
            self.validate_route_to_dest_on_source(
                src_route_tables,
                src_vpc_route_tables,
                dest_subnet_cidrs,
                b_check_vpc_rtb_ec2,
            )

            if len(self.rds_rtb_list) > 0:
                self.fail_json(
                    msg="Please review route table(s) {0} for entries matching {1} Cidr".format(
                        self.rds_rtb_list, src_private_ips
                    )
                )

            if len(self.ec2_rtb_list) > 0:
                self.fail_json(
                    msg="Please review route table(s) {} for entries matching {} Cidr".format(
                        self.ec2_rtb_list, dest_subnet_cidrs
                    )
                )

            self.exit_json(result="Route table validation successful")

        except Exception as e:
            self.fail_json(
                msg="Route table validation failed: {0}".format(e), exception=e
            )


def main():

    ValidateRouteTables()


if __name__ == "__main__":
    main()
