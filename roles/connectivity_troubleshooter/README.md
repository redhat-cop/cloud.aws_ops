Role Name
=========

A role to troubleshoot connectivity issues between the following:
- AWS resources within an Amazon Virtual Private Cloud (Amazon VPC);
- AWS resources in different Amazon VPCs within the same AWS Region that are connected using VPC peering;
- AWS resources in an Amazon VPC and an internet resource using an internet gateway;
- AWS resources in an Amazon VPC and an internet resource using a network address translation (NAT) gateway.

Requirements
------------

Authentication against AWS is managed by the `aws_setup_credentials` role.

It also requires the folllowing roles:
- connectivity_troubleshooter_validate
- connectivity_troubleshooter_igw
- connectivity_troubleshooter_local 
- connectivity_troubleshooter_nat
- connectivity_troubleshooter_peering

Role Variables
--------------

**connectivity_troubleshooter_destination_ip**: (Required) The IPv4 address of the resource you want to connect to.
**connectivity_troubleshooter_destination_port**: (Required) The port number you want to connect to on the destination resource.
**connectivity_troubleshooter_destination_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity to.
**connectivity_troubleshooter_source_ip**: (Required) The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_source_port_range**: (Optional) The port range used by the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_source_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity from.

Dependencies
------------

- role: aws_setup_credentials

Example Playbook
----------------

    - hosts: localhost

      roles:
        - role: cloud.aws_roles.connectivity_troubleshooter:
          connectivity_troubleshooter_destination_ip: 172.31.2.8
          connectivity_troubleshooter_destination_port: 443
          connectivity_troubleshooter_source_ip: 172.31.2.7

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.azure_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
