replicate_existing_rds_instance
==================

A role to set up an RDS read replica from an existing RDS instance.

Requirements
------------

AWS User Account with the following permission:

* rds:CreateDBInstanceReadReplica
* rds:ListTagsForResource
* rds:DescribeDBInstances

Role Variables
--------------

* **replicate_existing_rds_instance_rds_instance_repli**: The name of the rds instance that will be replicated. **Required**
* **replicate_existing_rds_instance_rds_instance_src**: The name of the replica rd instance.  **Required**

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for creating rds replica using cloud.aws_ops.create_rds_replica_from_existing_rds_instance role
  hosts: localhost
  gather_facts: false
  tasks:
    # Replicating source RDS instance ========================================================
    - name: Move one object between buckets
      ansible.builtin.include_role:
        name: cloud.aws_ops.create_rds_replica_from_existing_rds_instance
      vars:
        create_rds_replica_instance_from_existing_rds_instance_rds_instance_repli: rds_instance_repli_name
        create_rds_replica_instance_from_existing_rds_instance_rds_instance_src: rds_instance_src_name
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team