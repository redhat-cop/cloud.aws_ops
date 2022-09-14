Role Name
=========

A role to troubleshoot connectivity issues between AWS resources in an Amazon VPC and an internet resource using a network address translation (NAT) gateway.

Requirements
------------

If you would like to use this role independently, you must first run the `connectivity_troubleshooter_validate` role to set the  `next_hop ` variable used by this role. You can follow the Example Playbook bellow or add the `connectivity_troubleshooter_validate` role as a dependency within this role's `meta/main.yml`. Authentications against AWS can also be handled by adding the `aws_setup_credentials` role as a dependency within this role's `meta/main.yml` file.

Role Variables
--------------

**connectivity_troubleshooter_nat_destination_ip**: (Required) The IPv4 address of the resource you want to connect to.
**connectivity_troubleshooter_nat_destination_port**: (Required) The port number you want to connect to on the destination resource.
**connectivity_troubleshooter_nat_source_ip**: (Required) The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_nat_source_port_range**: (Optional) The port range used by the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_nat_source_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity from.

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: localhost

      roles:
        - role: connectivity_troubleshooter_validate
          connectivity_troubleshooter_validate_destination_ip: 172.31.2.8
          connectivity_troubleshooter_validate_destination_port: 443
          connectivity_troubleshooter_validate_source_ip: 172.31.2.7

        - role: cloud.aws_roles.connectivity_troubleshooter_nat:
          connectivity_troubleshooter_nat_destination_ip: 172.31.2.8
          connectivity_troubleshooter_nat_destination_port: 443
          connectivity_troubleshooter_nat_source_ip: 172.31.2.7

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
