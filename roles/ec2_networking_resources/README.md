ec2_networking_resources
====================

The `ec2_networking_resources` role allows you to create a basic set of networking resources in which you can run EC2 instances. By default, the subnet that is created is set to allow SSH access from within the VPC.

Requirements
------------

An AWS account with the following permissions:

* ec2:AssociateRouteTable
* ec2:AuthorizeSecurityGroupIngress
* ec2:CreateRouteTable
* ec2:CreateSecurityGroup
* ec2:CreateSubnet
* ec2:CreateVpc
* ec2:DescribeRouteTables
* ec2:DescribeSecurityGroups
* ec2:DescribeSubnets
* ec2:DescribeTags
* ec2:DescribeVpcAttribute
* ec2:DescribeVpcs
* ec2:ModifyVpcAttribute
* sts:GetCallerIdentity

Role Variables
--------------

* **ec2_networking_resources_vpc_name**: (Required) The name of the VPC to create.
* **ec2_networking_resources_vpc_cidr_block**: (Required) The CIDR block to use for the VPC being created.
* **ec2_networking_resources_subnet_cidr_block**: (Required) The CIDR block to use for subnet being created.
* **ec2_networking_resources_sg_internal_name**: (Required) The name of the security group to create.
* **ec2_networking_resources_sg_internal_description**: (Required) The description of the security group being created.
* **ec2_networking_resources_sg_internal_rules**: (Optional) List of rules to apply to the security group being created. By default, a rule allowing SSH access from within the VPC will be added. A rule should contain the following keys:
    * **proto** (str): The IP protocol name.
    * **ports** (str): A list of ports traffic is going to. Can be a single port, or a range of ports, for example, 8000-8010.
    * **cidr_ip** (str): The CIDR block traffic is coming from.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

```yaml
- hosts: localhost
  roles:
    - role: cloud.aws_ops.ec2_networking_resources
      vars:
        ec2_networking_resources_vpc_name: my-vpn
        ec2_networking_resources_vpc_cidr_block: 10.0.1.0/16
        ec2_networking_resources_subnet_cidr_block: 10.0.1.0/26
        ec2_networking_resources_sg_internal_name: my-sg
        ec2_networking_resources_sg_internal_description: My internal security group
        ec2_networking_resources_sg_internal_rules:
          - proto: tcp
            ports: 22
            cidr_ip: 10.0.1.0/16
          - ports: tcp
            ports: 8000-8010
            cidr_ip: 10.0.1.0/16
```

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
