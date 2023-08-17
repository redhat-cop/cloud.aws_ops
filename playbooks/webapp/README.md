# cloud.amazon_roles.webapp

A playbook to create, delete, or migrate a webapp on AWS.

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

* **operation**: Operation for the webapp playbook to perform, either `create` or `delete`. Default: `create`
* **resource_prefix**: (Required) A prefix to prepend to the name of all AWS resources created for the webapp
* **resource_tags**: Tags to apply to all AWS resources created for the webapp. Default: `prefix: "{{ resource_prefix }}"`
* **aws_access_key**: (Required) AWS access key ID for user account with the above permissions
* **aws_secret_key**: (Required) AWS secret access key for user account with the above permissions
* **aws_region**: (Required) AWS region in which to create webapp resources
* **dest_region**: AWS region to migrate the webapp to, only used when migrating an existing webapp
* **delete_source**: Whether to delete the source region webapp resources when migrating an existing webapp. Default: `false`
* **security_token**: Security token for AWS session authentication

### EC2 instance

* **image_filter**: Name of AWS AMI to use. Default: `Fedora-Cloud-Base-35-*`
* **sshkey_pair_name**: Name for the EC2 key pair. Default: `"{{ resource_prefix }}-key"`
* **bastion_host_name**: Name for the EC2 instance. Default: `"{{ resource_prefix }}-bastion"`
* **bastion_host_type**: Instance type for the EC2 instance. Default: `t2.xlarge`
* **bastion_host_username**: Username for the bastion host SSH user. Default: `fedora`
* **bastion_host_required_packages**: Packages to be installed on the bastion host. Default:
  ```yaml
  - python3
  - python-virtualenv
  - sshpass
  - git
  - podman
  - httpd-tools
  - ansible
  ```

### Networking

* **vpc_name**: Name for the VPC. Default: `"{{ resource_prefix }}-vpc"`
* **vpc_cidr**: IPv4 address range for the VPC. Default: `10.1.0.0/16`
* **subnet_cidr**: Subnet CIDR blocks - a public subnet for the bastion host, private subnets for workers and RDS instance. Default:
  ```yaml
  - 10.1.0.0/24
  - 10.1.1.0/24
  - 10.1.2.0/24
  ```
* **rds_subnet_group_name**: Subnet group name for the RDS instance. Default: `"{{ resource_prefix }}-rds-sg"`
* **rds_secgroup_name**: Security group name for the RDS instance. Default: `"{{ resource_prefix }}-rds-sec"`
* **public_secgroup_name**: Security group name for the bastion host. Default: `"{{ resource_prefix }}-sg"`
* **app_listening_port**: Connection listening port for the app on the bastion host. Default: `5000`
* **rds_listening_port**: Connection listening port for the RDS instance. Default: `5432`

### RDS instance

* **rds_snapshot_arn**: If provided, will create an RDS instance from an existing snapshot. Default: `null`
* **rds_identifier**: Unique identifier for the RDS instance. Default: `"{{ resource_prefix }}-rds-01"`
* **rds_allocated_storage_gb**: The amount of storage (in GB) to allocate for the DB instance. Default: `20`
* **rds_instance_class**: DB instance class for the RDS instance. Default: `db.m6g.large`
* **rds_instance_name**: Name for the database. Default: `mysampledb123`
* **rds_engine**: Engine to use for the database. Default: `postgres`
* **rds_engine_version**: Version number of the database engine to use. Default: `"14.8"`
* **rds_master_user**: Name of the master user for the database instance. Default: `ansible`
* **rds_master_password**: Password for the master database user. Default: `L#5cH2mgy_`

### Webapp

* **app_git_repository**: Git repository for the webapp. Default: `https://github.com/abikouo/webapp_pyflask_demo.git`
* **number_of_workers**: Number of worker instances to create. Default: `2`
* **workers_instance_type**: EC2 instance type for workers. Default: `t2.large`
* **local_registry_user**: Username for local Podman registry. Default: `ansible`
* **local_registry_pwd**: Password for local Podman registry. Default: `testing123`
* **local_registry_port**: Port for the local Podman registery. Default: `"{{ app_listening_port }}"`
* **app_config**: Configuration values for the webapp, passed as corresponding env variables FLASK_APP, FLASK_ENV, ADMIN_USER, and ADMIN_PASSWORD when the app is deployed. Default:
  ```yaml
  app_dir: /app/pyapp
  env: development
  admin_user: admin
  admin_password: admin
  ```
* **app_force_init**: Whether to drop existing tables and create new ones when deploying the webapp database. Default: `false`

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
