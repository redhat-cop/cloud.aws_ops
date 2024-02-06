create_rds_global_cluster
=========

A role to create an Amazon Aurora global cluster with two different region rds clusters.

Creates the following resources:
1. Global Cluster - Amazon Aurora Postgresql or Amazon Aurora MySql cluster. If `create_rds_global_cluster_engine` is not provided, defaults to Amazon Aurora Postgresql.
2. Primary Cluster - Primary cluster in specified region (`create_rds_global_cluster_primary_cluster_region`).
3. Primary Cluster Instance - Instance in the primary cluster.
4. Replica (secondary) Cluster - Secondary cluster in specified region (`create_rds_global_cluster_replica_cluster_region`).
5. Replica Cluster Instance - Instance in the replica cluster.

Please refer to [Role Variables](#role-variables) for variables and usage.

Requirements
------------

AWS User Account with the following permissions:

* rds:CreateGlobalCluster
* rds:DeleteGlobalCluster
* rds:ModifyGlobalCluster
* rds:CreateDBCluster
* rds:DeleteDBCluster
* rds:ModifyDBCluster
* rds:DescribeGlobalClusters
* rds:DescribeDBClusters

Role Variables
--------------
**Global cluster variables**
- **create_rds_global_cluster_global_cluster_name** - Name of the Amazon Aurora global cluster. **required**
- **create_rds_global_cluster_engine** - Engine of the Amazon Aurora global and rds clusters. Default is aurora-postgresql.
- **create_rds_global_cluster_engine_version** - Engine version of the Amazon Aurora global and rds clusters.
- **create_rds_global_cluster_instance_class** - Instance class of instance in primary and replica cluster. **Required** when __create_rds_global_cluster_operation__ is set to __create__.
- **create_rds_global_cluster_master_username** - Username of the rds clusters master user. **Required** when __create_rds_global_cluster_operation__ is set to __create__.
- **create_rds_global_cluster_master_user_password** - Password of the rds clusters master user. **Required** when __create_rds_global_cluster_operation__ is set to __create__.

**Primary cluster variables**
- **create_rds_global_cluster_primary_cluster_name** - Name of the primary cluster. Default is $create_rds_global_cluster_global_cluster_name.
- **create_rds_global_cluster_primary_cluster_region** - Region of the primary cluster. **required**
- **create_rds_global_cluster_primary_cluster_instance_name** - Name of the instance in primary cluster. **required**
- **create_rds_global_cluster_primary_cluster_db_name** - The name for your database of up to 64 alphanumeric characters. If not provided, database is not created in the cluster.
- **create_rds_global_cluster_primary_cluster_vpc_security_group_ids** - A list of EC2 VPC security groups to associate with the primary DB cluster.
- **create_rds_global_cluster_db_subnet_group_name** - A DB subnet group to associate with this DB cluster if not using the default.

**Replica cluster variables**
- **create_rds_global_cluster_replica_cluster_name** - Name of the replica (secondary) cluster. Default is create_rds_global_cluster_global_cluster_name.
- **create_rds_global_cluster_replica_cluster_region** - Region of the replica (secondary) cluster. **required**
- **create_rds_global_cluster_replica_cluster_instance_name** - Name of the instance in secondary cluster. **required**
- **create_rds_global_cluster_replica_enable_global_write_forwarding** - Whether to enable replica cluster to forward write operations to the primary cluster of an Amazon Aurora global database. Default is False. Supported only while creating new cluster. Choices include 'true', 'false, 'yes', 'no'.
- **create_rds_global_cluster_replica_cluster_vpc_security_group_ids** -  A list of EC2 VPC security groups to associate with the replica DB cluster.

- **create_rds_global_cluster_operation** - Choices include 'create' and 'delete' to create or delete the resources.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------
```
---
- name: Playbook for demonstrating use of cloud.aws_ops.create_rds_global_cluster role
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create global db, primary cluster with instance & replica cluster with instance
      ansible.builtin.include_role:
        name: cloud.aws_ops.create_rds_global_cluster
      vars:
        create_rds_global_cluster_operation: create
        create_rds_global_cluster_engine: aurora-mysql
        create_rds_global_cluster_engine_version: 5.7
        create_rds_global_cluster_instance_class: db.r5.large
        create_rds_global_cluster_master_username: testusername
        create_rds_global_cluster_master_user_password: test-password_rds
        create_rds_global_cluster_global_cluster_name: test-cluster-global
        create_rds_global_cluster_primary_cluster_name: test-cluster-primary
        create_rds_global_cluster_primary_cluster_region: eu-central-1
        create_rds_global_cluster_primary_cluster_instance_name: test-instance-primary
        create_rds_global_cluster_replica_cluster_name: test-cluster-replica
        create_rds_global_cluster_replica_cluster_region: us-west-2
        create_rds_global_cluster_replica_enable_global_write_forwarding: true
        create_rds_global_cluster_replica_cluster_instance_name: test-instance-replica
        create_rds_global_cluster_primary_cluster_db_name: MyPrimaryDb
        create_rds_global_cluster_primary_cluster_vpc_security_group_ids: [ "sg-03bfd123456789012", "sg-03bfd123456789034"]
        create_rds_global_cluster_replica_cluster_vpc_security_group_ids: ["sg-03bfd123456789055"]

    - name: Delete global db, primary cluster with instance & replica cluster with instance
      ansible.builtin.include_role:
        name: cloud.aws_ops.create_rds_global_cluster
      vars:
        create_rds_global_cluster_operation: delete
        create_rds_global_cluster_global_cluster_name: test-cluster-global
        create_rds_global_cluster_primary_cluster_name: test-cluster-primary
        create_rds_global_cluster_primary_cluster_region: eu-central-1
        create_rds_global_cluster_primary_cluster_instance_name: test-instance-primary
        create_rds_global_cluster_replica_cluster_name: test-cluster-replica
        create_rds_global_cluster_replica_cluster_region: us-west-2
        create_rds_global_cluster_replica_cluster_instance_name: test-instance-replica
```

License
-------
GNU General Public License v3.0 or later
