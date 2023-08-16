create_rds_global_cluster
=========

A role to create Amazon Aurora global cluster with two different region rds clusters.

Creates following resources
1. Global Cluster - Amazon Aurora Postgresql.
2. Primary Cluster - Primary cluster in specified region (create_rds_global_cluster_primary_cluster_region).
3. Primary Cluster Instance - Instance in the primary cluster.
4. Replica (secondary) Cluster - Secondary cluster in specified region (create_rds_global_cluster_replica_cluster_region).
5. Replica Cluster Instance - Instance in the replica cluster.

Requirements
------------

AWS credentials with valid permission.

Role Variables
--------------
**Global cluster variables**
- **create_rds_global_cluster_global_cluster_name** - Name of the Amazon Aurora global cluster. **required**
- **create_rds_global_cluster_engine** - Engine of the Amazon Aurora global and rds clusters. Default is aurora-postgresql.
- **create_rds_global_cluster_engine_version** - Engine version of the Amazon Aurora global and rds clusters.
- **create_rds_global_cluster_instance_class** - Instance class of instance in primary and replica cluster. **required**
- **create_rds_global_cluster_username** - Username of the rds clusters. **required**
- **create_rds_global_cluster_password** - Password of the rds clusters. **required**

**Primary cluster variables**
- **create_rds_global_cluster_primary_cluster_name** - Name of the primary cluster. Default is $create_rds_global_cluster_global_cluster_name.
- **create_rds_global_cluster_primary_cluster_region** - Region of the primary cluster. **required**
- **create_rds_global_cluster_primary_cluster_instance_name** - Name of the instance in primary cluster. **required**

**Replica cluster variables**
- **create_rds_global_cluster_replica_cluster_name** - Name of the replica (secondary) cluster. Default is create_rds_global_cluster_global_cluster_name.
- **create_rds_global_cluster_replica_cluster_region** - Region of the replica (secondary) cluster. **required**
- **create_rds_global_cluster_replica_cluster_instance_name** - Name of the instance in secondary cluster. **required**
- **create_rds_global_cluster_replica_enable_global_write_forwarding** - Whether to enable replica cluster to forward write operations to the primary cluster of an Amazon Aurora global database. Default is False. Supported only while creating new cluster. Choices include 'true', 'false, 'yes', 'no'.
- **create_rds_global_cluster_operation** - Choices include 'create' and 'delete' to create or delete the resources.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

License
-------
GNU General Public License v3.0 or later
