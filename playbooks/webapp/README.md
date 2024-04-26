# cloud.aws_ops.webapp playbooks

Playbooks to create or delete, or migrate a webapp on AWS.

## Requirements

AWS User Account with the following permissions:

To create or migrate the webapp:

* ec2:AllocateAddress
* ec2:AssociateRouteTable
* ec2:AttachInternetGateway
* ec2:AuthorizeSecurityGroupIngress
* ec2:CreateInternetGateway
* ec2:CreateKeyPair
* ec2:CreateNatGateway
* ec2:CreateRoute
* ec2:CreateRouteTable
* ec2:CreateSecurityGroup
* ec2:CreateSubnet
* ec2:CreateTags
* ec2:CreateVpc
* ec2:DescribeAvailabilityZones
* ec2:DescribeImages
* ec2:DescribeInstanceAttribute
* ec2:DescribeInstanceStatus
* ec2:DescribeInstances
* ec2:DescribeInternetGateways
* ec2:DescribeKeyPairs
* ec2:DescribeNatGateways
* ec2:DescribeRouteTables
* ec2:DescribeSecurityGroups
* ec2:DescribeSubnets
* ec2:DescribeTags
* ec2:DescribeVpcAttribute
* ec2:DescribeVpcs
* ec2:ModifyVpcAttribute
* ec2:RunInstances
* rds:CreateDBInstance
* rds:CreateDBSubnetGroup
* rds:DescribeDBInstances
* rds:DescribeDBSubnetGroups
* rds:ListTagsForResource
* rds:RestoreDBInstanceFromDBSnapshot (if migrating an app or restoring the app database from a snapshot)
* sts:GetCallerIdentity

To delete the webapp:

* ec2:DeleteInternetGateway
* ec2:DeleteKeyPair
* ec2:DeleteNatGateway
* ec2:DeleteRouteTable
* ec2:DeleteSecurityGroup
* ec2:DeleteSubnet
* ec2:DeleteVpc
* ec2:DescribeInstances
* ec2:DescribeInternetGateways
* ec2:DescribeKeyPairs
* ec2:DescribeNatGateways
* ec2:DescribeNetworkInterfaces
* ec2:DescribeRouteTables
* ec2:DescribeSecurityGroups
* ec2:DescribeSubnets
* ec2:DescribeTags
* ec2:DescribeVpcAttribute
* ec2:DescribeVpcs
* ec2:DetachInternetGateway
* ec2:DisassociateRouteTable
* ec2:TerminateInstances
* elasticloadbalancing:DeleteLoadBalancer
* elasticloadbalancing:DescribeInstanceHealth
* elasticloadbalancing:DescribeLoadBalancerAttributes
* elasticloadbalancing:DescribeLoadBalancerPolicies
* elasticloadbalancing:DescribeLoadBalancers
* rds:DeleteDBInstance
* rds:DeleteDBSubnetGroup
* rds:DescribeDBInstances
* rds:DescribeDBSubnetGroups
* rds:ListTagsForResource
* sts:GetCallerIdentity

## Playbook Variables

### Common

* **operation** (str): Operation for the webapp playbook to perform, either `create` or `delete`. Default: `create`
* **resource_prefix** (str): A prefix to prepend to the name of all AWS resources created for the webapp. Default: `ansible-test`
* **resource_tags** (dict, elements dict): Tags to apply to all AWS resources created for the webapp. Default: `prefix: "{{ resource_prefix }}"`
* **aws_access_key** (str): (Required) AWS access key ID for user account with the above permissions
* **aws_secret_key** (str): (Required) AWS secret access key for user account with the above permissions
* **aws_region** (str): (Required) AWS region in which to create webapp resources
* **dest_region** (str): AWS region to migrate the webapp to, only used when migrating an existing webapp
* **delete_source** (bool): Whether to delete the source region webapp resources when migrating an existing webapp. Default: `false`
* **security_token** (str): Security token for AWS session authentication

### EC2 instance

* **image_filter** (str): Name of AWS AMI to use. Default: `Fedora-Cloud-Base-35-*`
* **deploy_flask_app_sshkey_pair_name** (str): Name for the EC2 key pair. Default: `"{{ resource_prefix }}-key"`
* **deploy_flask_app_bastion_host_name** (str): Name for the EC2 instance. Default: `"{{ resource_prefix }}-bastion"`
* **bastion_host_type** (str): Instance type for the EC2 instance. Default: `t2.xlarge`
* **deploy_flask_app_bastion_host_username** (str): Username for the bastion host SSH user. Default: `fedora`

### Networking

* **vpc_name** (str): Name for the VPC. Default: `"{{ resource_prefix }}-vpc"`
* **vpc_cidr** (str): IPv4 address range for the VPC. Default: `10.1.0.0/16`
* **subnet_cidr** (list, elements str): Subnet CIDR blocks - a public subnet for the bastion host, private subnets for workers and RDS instance. Default:
  ```yaml
  - 10.1.0.0/24
  - 10.1.1.0/24
  - 10.1.2.0/24
  ```
* **rds_subnet_group_name** (str): Subnet group name for the RDS instance. Default: `"{{ resource_prefix }}-rds-sg"`
* **rds_secgroup_name** (str): Security group name for the RDS instance. Default: `"{{ resource_prefix }}-rds-sec"`
* **public_secgroup_name** (str): Security group name for the bastion host. Default: `"{{ resource_prefix }}-sg"`
* **deploy_flask_app_listening_port** (int): Connection listening port for the app on the bastion host. Default: `5000`
* **rds_listening_port** (int): Connection listening port for the RDS instance. Default: `5432`

### RDS instance

* **rds_snapshot_arn** (str): If provided, will create an RDS instance from an existing snapshot. Default: `null`
* **rds_identifier** (str): Unique identifier for the RDS instance. Default: `"{{ resource_prefix }}-rds-01"`
* **rds_allocated_storage_gb** (int): The amount of storage (in GB) to allocate for the DB instance. Default: `20`
* **rds_instance_class** (str): DB instance class for the RDS instance. Default: `db.m6g.large`
* **rds_instance_name** (str): Name for the database. Default: `mysampledb123`
* **rds_engine** (str): Engine to use for the database. Default: `postgres`
* **rds_engine_version** (str): Version number of the database engine to use. Default: `"16.2"`
* **deploy_flask_app_rds_master_username** (str): Name of the master user for the database instance. Default: `ansible`
* **deploy_flask_app_rds_master_password** (str): Password for the master database user. Default: `L#5cH2mgy_`

### Webapp

* **deploy_flask_app_number_of_workers** (int): Number of worker instances to create. Default: `2`
* **deploy_flask_app_workers_instance_type** (str): EC2 instance type for workers. Default: `t2.xlarge`
* **deploy_flask_app_config** (dict, elements dict): Configuration values for the webapp, passed as corresponding env variables FLASK_APP, FLASK_ENV, ADMIN_USER, and ADMIN_PASSWORD when the app is deployed. Default:
  ```yaml
  app_dir: /app/pyapp
  env: development
  admin_user: admin
  admin_password: admin
  ```
* **deploy_flask_app_force_init** (bool): Whether to drop existing tables and create new ones when deploying the webapp database. Default: `false`

### webapp deployment in HA architecture

`webapp_ha_aurora.yaml` playbook deploys the flask app to a cross region high availability architecture. The playbook replicates the app deployment to a second region. The backend is an Aurora global cluster. For adding the write forwarding feature, aurora-mysql can be used. Default db engine is aurora-postgresql. The app in each region is configured to access the associated Aurora cluster. In front of the two regions, route53 records are added to provide cross region DNS (failover scenario).

Along with the [above](README.md#playbook-variables) variables, following variables are needed for this playbook:

* **rds_instance_class** (str): DB instance class for the aurora db instances. Default: `db.r5.large`
* **rds_global_cluster_name** (str): Name of the global cluster. Default: "{{ resource_prefix }}-global-cluster"
* **rds_primary_cluster_name** (str): Name of the primary cluster. Default: "{{ resource_prefix }}-primary-cluster"
* **rds_primary_cluster_region** (str): Primary Region. Default: `us-west-2`
* **rds_primary_cluster_instance_name** (str): Name of primary db instance. Default: "{{ resource_prefix }}-primary-instance"
* **rds_replica_cluster_name** (str): Name of the replica cluster. Default: "{{ resource_prefix }}-replica-cluster"
* **rds_replica_cluster_region** (str): Replica Region. Default: `us-east-2`
* **rds_replica_cluster_instance_name** (str): Name of the replica db instance. Default: "{{ resource_prefix }}-replica-instance"

#### vars for route53 records
* **route53_zone_name** (str): (required) Route53 Zone name.
* **route53_subdomain** (str): Sub domain name for the application url. Default: "flaskapp"

## Example Usage

Create a `credentials.yaml` file with the folling contents:

```yaml
aws_access_key: "xxxxxxxxxxxxxxxxxxxx"
aws_secret_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aws_region: "us-east-1"
resource_prefix: sample-prefix
```

To create a webapp, run:

```bash
ansible-playbook webapp.yaml -e "@credentials.yaml"
```

To delete the webapp resources created above, run:

```bash
ansible-playbook webapp.yaml -e "@credentials.yaml" -e "operation=delete"
```

To migrate a webapp from one region to another, run:

```bash
ansible-playbook migrate_webapp.yaml -e "@credentials.yaml" -e "dest_region=my-new-region"
```

Note: migrating a webapp does not delete the app resources from the source region by default. To delete the source webapp, set var `delete_source: true`.

To deploy the app in a high availability architecture, run:

```bash
ansible-playbook webapp_ha_aurora.yaml -e "@credentials.yaml" -e "operation=create"
```

To delete the webapp resources created by the above playbook, run:

```bash
ansible-playbook webapp_ha_aurora.yaml -e "@credentials.yaml" -e "operation=delete"
```

