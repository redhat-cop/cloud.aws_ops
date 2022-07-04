troubleshoot_rds_connectivity
==================

A role to troubleshoot RDS connectivity from an EC2 instance.

Requirements
------------

N/A

Role Variables
--------------

* **troubleshoot_rds_connectivity_db_instance_id**: The DB instance ID to test connectivity to.
* **troubleshoot_rds_connectivity_ec2_instance_id**: The ID of the EC2 instance to test connectivity from.

Dependencies
------------

- role: aws_setup_credentials

Example Playbook
----------------

    - hosts: localhost

      roles:
        - role: cloud.aws_roles.troubleshoot_rds_connectivity
          troubleshoot_rds_connectivity_db_instance_id: my-db_instance_id
          troubleshoot_rds_connectivity_ec2_instance_id: ec2-instance-dx

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.azure_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team