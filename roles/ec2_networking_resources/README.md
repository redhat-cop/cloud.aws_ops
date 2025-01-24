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

* **ec2_networking_resources_operation**: (Optional) Target operation for the networking resources role. Choices are ["create", "delete"]. Defaults to "create".
* **ec2_networking_resources_vpc_name**: (Required) The name of the VPC to create or delete.
* **ec2_networking_resources_vpc_cidr_block**: (Optional) The CIDR block to use for the VPC being created. Required if `ec2_networking_resources_operation` is "create".
* **ec2_networking_resources_subnet_cidr_block**: (Optional) The CIDR block to use for subnet being created. Required if `ec2_networking_resources_operation` is "create".
* **ec2_networking_resources_sg_name**: (Optional) The name of the security group to create. Required if `ec2_networking_resources_operation` is "create".
* **ec2_networking_resources_sg_description**: (Optional) The description of the security group being created. Defaults to "Security group for EC2 instance".
* **ec2_networking_resources_sg_rules**: (Optional) List of rules to apply to the security group being created. By default, a rule allowing SSH access from within the VPC will be added. A rule should contain the following keys:
  * **proto** (str): The IP protocol name.
  * **ports** (list): A list of ports traffic is going to. Can be a single port or a range of ports, for example 8000-8010.
  * **cidr_ip** (str): The CIDR block traffic is coming from.
* **ec2_networking_resources_create_igw**: (Optional) Whether to create an internet gateway and route traffic to it. Defaults to `false`.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Examples
----------------

Create networking resources with an internet gateway and allow HTTP/HTTPS traffic:

```yaml
- hosts: localhost
  roles:
    - role: cloud.aws_ops.ec2_networking_resources
      vars:
        ec2_networking_resources_vpc_name: my-vpn
        ec2_networking_resources_vpc_cidr_block: 10.0.1.0/16
        ec2_networking_resources_subnet_cidr_block: 10.0.1.0/26
        ec2_networking_resources_sg_name: my-sg
        ec2_networking_resources_sg_description: My security group
        ec2_networking_resources_sg_rules:
          - proto: tcp
            ports: 22
            cidr_ip: 10.0.1.0/16
          - ports: tcp
            ports: 80
            cidr_ip: 0.0.0.0/0
          - proto: tcp
            ports: 443
            cidr_ip: 0.0.0.0/0
        ec2_networking_resources_create_igw: true
```

Delete networking resources:

```yaml
- hosts: localhost
  roles:
    - role: cloud.aws_ops.ec2_networking_resources
      vars:
        ec2_networking_resources_operation: delete
        ec2_networking_resources_vpc_name: my-vpn
```

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
