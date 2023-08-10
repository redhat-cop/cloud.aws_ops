create_rds_global_cluster
=========

A role to create aurora-postgresql global cluster with two different region rds clusters.

Requirements
------------

AWS credentials with valid permission.

Role Variables
--------------
* **global_cluster_identifier** - Name of the Aurora global cluster. **Required**
* **cluster_id** - Name of the primary cluster. **Required**
* **username** - Username of the rds clusters. **Required**
* **password** - Password of the rds clusters. **Required**
* **engine** - Engine of the global and rds clusters. **Required**
* **db_instance_class** - A DB instance class type and size. **Required**
* **region_src** - The primary cluster region. **Required**
* **region_dest** - The secondary cluster region. **Required**
* **db_subnet_group_name** - The name of subnet group.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------
---
- name: Playbook for move objects between buckets using cloud.aws_ops.move_objects_between_buckets role
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Move one object between buckets
      ansible.builtin.include_role:
        name: cloud.aws_ops.move_objects_between_buckets
      vars:
        global_cluster_identifier: global_cluster_name
        cluster_id: cluster_name
        username: username
        password: password123
        engine: aurora-postgresql
        db_subnet_group_name: subnet_group_name
        db_instance_class: db.r5.large
        region_primary: us-east-2
        region_secondary: us-east-1
        instance_id: instance_id_name

License
-------
GNU General Public License v3.0 or later
