====================================================
CHANGE THIS IN changelogs/config.yaml! Release Notes
====================================================

.. contents:: Topics


v3.2.0
======

Release Summary
---------------

This release adds an optional credential field to contoller_projects in ``configure_ec2`` pattern and updates ansible-lint version.

Minor Changes
-------------

- Add an optional credential field to support attaching an SCM credential when creating controller_projects. (https://github.com/redhat-cop/cloud.aws_ops/pull/156)
- Bump version of ansible-lint to 25.1.2 (https://github.com/redhat-cop/cloud.aws_ops/pull/159).

v3.1.0
======

Release Summary
---------------

This release adds a new role ``ec2_networking_resources`` and a pattern for creating an ec2 instance.

Minor Changes
-------------

- update FQCN for modules that were migrated from community.aws to amazon.aws (https://github.com/redhat-cop/cloud.aws_ops/pull/120).

New Roles
---------

- ec2_networking_resources - A role to create a basic networking environment for an EC2 instance.

v3.0.0
======

Release Summary
---------------

This release fixes bug on roles, remove support for ansible-core < 2.15.

Breaking Changes / Porting Guide
--------------------------------

- Bump minimum version requirement for ansible-core to 2.15 (https://github.com/redhat-cop/cloud.aws_ops/pull/114).
- roles/deploy_flask_app - Add parameter ``deploy_flask_app_bastion_ssh_private_key`` to define the path to the ssh private key file to use to connect to the bastion host (https://github.com/redhat-cop/cloud.aws_ops/issues/109).
- roles/deploy_flask_app - The following parameters no longer required have been removed ``deploy_flask_app_bastion_host_required_packages``, ``deploy_flask_app_local_registry_port``, ``deploy_flask_app_local_registry_pwd``, ``deploy_flask_app_local_registry_user``, ``deploy_flask_app_git_repository`` (https://github.com/redhat-cop/cloud.aws_ops/issues/103).

Minor Changes
-------------

- Bump version of ansible-lint to minimum 24.7.0 (https://github.com/redhat-cop/cloud.aws_ops/pull/114).
- Replace the postgres db engine version from 14.8 to 16.2

Bugfixes
--------

- Fix incorrect dict attribute in backup_select_resources role.

v2.0.0
======

Release Summary
---------------

This release fixes bug on roles, remove support for ansible-core < 2.14 and introduces new features.

Breaking Changes / Porting Guide
--------------------------------

- Remove support for ansible-core < 2.14
- playbooks/webapp/deploy_flask_app - convert playbook to role (https://github.com/redhat-cop/cloud.aws_ops/pull/85).
- playbooks/webapp/migrate_webapp - replace variable name `do_not_delete_source` with `delete_source` to make intent clearer and fix reversed default value logic (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- playbooks/webapp/webapp - Rename the playbook vars with role name prefix. 'sshkey_pair_name' changed to 'deploy_flask_app_sshkey_pair_name' 'bastion_host_name' changed to 'deploy_flask_app_bastion_host_name' 'bastion_host_username' changed to 'deploy_flask_app_bastion_host_username' 'bastion_host_required_packages' changed to 'deploy_flask_app_bastion_host_required_packages' 'app_listening_port' changed to 'deploy_flask_app_listening_port' 'rds_master_user' changed to 'deploy_flask_app_rds_master_username' 'rds_master_password' changed to 'deploy_flask_app_rds_master_password' 'app_git_repository' changed to 'deploy_flask_app_git_repository' 'number_of_workers' changed to 'deploy_flask_app_number_of_workers' 'workers_instance_type' changed to 'deploy_flask_app_workers_instance_type' 'local_registry_user' changed to 'deploy_flask_app_local_registry_user' 'local_registry_pwd' changed to 'deploy_flask_app_local_registry_pwd' 'local_registry_port' changed to 'deploy_flask_app_local_registry_port' 'app_config' changed to 'deploy_flask_app_config' 'app_force_init' changed to 'deploy_flask_app_force_init' (https://github.com/redhat-cop/cloud.aws_ops/pull/85).
- role/aws_setup_credentials - Due to ansible-lint issue, the AWS generated credentials are now stored into variable `aws_setup_credentials__output` instead of `aws_role_credentials`  (https://github.com/redhat-cop/cloud.aws_ops/pull/39).
- roles/awsconfig_multiregion_cloudtrail - ``bucket_name`` option has been renamed to ``awsconfig_multiregion_cloudtrail_bucket_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/awsconfig_multiregion_cloudtrail - ``key_prefix`` option has been renamed to ``awsconfig_multiregion_cloudtrail_key_prefix`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/awsconfig_multiregion_cloudtrail - ``operation`` option has been renamed to ``awsconfig_multiregion_cloudtrail_operation`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/awsconfig_multiregion_cloudtrail - ``trail_name`` option has been renamed to ``awsconfig_multiregion_cloudtrail_trail_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``plan_name`` option has been renamed to ``backup_create_plan_plan_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``plan_rules`` option has been renamed to ``backup_create_plan_plan_rules`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``plan_tags`` option has been renamed to ``backup_create_plan_plan_tags`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``plan_windows_vss_settings`` option has been renamed to ``backup_create_plan_plan_windows_vss_settings`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``vault_encryption_key_arn`` option has been renamed to ``backup_create_plan_vault_encryption_key_arn`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``vault_name`` option has been renamed to ``backup_create_plan_vault_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_create_plan - ``vault_tags`` option has been renamed to ``backup_create_planvault_tags`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_select_resources - ``backup_role_name`` option has been renamed to ``backup_select_resources_backup_role_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_select_resources - ``plan_name`` option has been renamed to ``backup_select_resources_plan_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_select_resources - ``selection_conditions`` option has been renamed to ``backup_select_resources_selection_conditions`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_select_resources - ``selection_name`` option has been renamed to ``backup_select_resources_selection_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/backup_select_resources - ``selection_tags`` option has been renamed to ``backup_select_resources_selection_tags`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``custom_ami_name`` option has been renamed to ``customized_ami_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``custom_ami_operation`` option has been renamed to ``customized_ami_operation`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``custom_ami_packages`` option has been renamed to ``customized_ami_packages`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``custom_ami_recreate_if_exists`` option has been renamed to ``customized_ami_recreate_if_exists`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``source_ami_filters`` option has been renamed to ``customized_ami_source_ami_filters`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``source_ami_image_id`` option has been renamed to ``customized_ami_source_ami_image_id`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/customized_ami - ``source_ami_user_name`` option has been renamed to ``customized_ami_source_ami_user_name`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/ec2_instance_terminate_by_tag - ``tag_key_to_terminate_instances`` option has been renamed to `` ec2_instance_terminate_by_tag_tag_key_to_terminate_instances`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/ec2_instance_terminate_by_tag - ``tag_value_to_terminate_instances`` option has been renamed to `` ec2_instance_terminate_by_tag_tag_value_to_terminate_instances`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/ec2_instance_terminate_by_tag - ``terminate_protected_instances`` option has been renamed to `` ec2_instance_terminate_by_tag_terminate_protected_instances`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/manage_transit_gateway - ``action`` option has been renamed to `` manage_transit_gateway_action`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/manage_transit_gateway - ``transit_gateway`` option has been renamed to `` manage_transit_gateway_transit_gateway`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/manage_transit_gateway - ``vpc_attachment`` option has been renamed to `` manage_transit_gateway_vpc_attachment`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).
- roles/manage_transit_gateway - ``vpn_attachment`` option has been renamed to `` manage_transit_gateway_vpn_attachment`` (https://github.com/redhat-cop/cloud.aws_ops/pull/84).

Minor Changes
-------------

- Add a playbook to deploy a simple flask web app into high availability architecture (https://github.com/redhat-cop/cloud.aws_ops/pull/97).
- awsconfig_apigateway_with_lambda_integration - new role to create API gateway with Lambda integration
- create_rds_global_cluster - new role to create aurora global cluster with a primary and a replica cluster in different regions.
- playbooks/upload_file_to_s3 - A playbook to upload file from local filesystem into S3 bucket (https://github.com/redhat-cop/cloud.aws_ops/pull/88).

Bugfixes
--------

- fix and update integration tests target test_manage_vpc_peering (https://github.com/redhat-cop/cloud.aws_ops/pull/61).
- playbooks/webapp/webapp - Update playbooks that include credentials to be able to be used with Automation Controller (not just the command line) (https://github.com/redhat-cop/cloud.aws_ops/pull/64).
- playbooks/webapp/webapp - update RDS engine from deprecated version (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- playbooks/webapp/webapp - update webapp create task to use provided variables instead of hard-coding values in some places (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- roles/aws_manage_cloudtrail_encryption - fix condition logic to match expected Cloudtrail events and add extra_vars to pass rulebook variables to playbooks called in actions (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- roles/aws_restore_cloudtrail - provide `key_prefix` default so it doesn't error if not present (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- roles/aws_restore_kms_key - fix conditional value to properly retrieve KMS key ARN from ansible-rulebook event variable (https://github.com/redhat-cop/cloud.aws_ops/pull/86).
- roles/aws_setup_credentials - add no_log to prevent credentials leak (https://github.com/redhat-cop/cloud.aws_ops/pull/92).
- roles/backup_select_resources - Add all necessary IAM service role policies for backup when creating a new IAM role (https://github.com/redhat-cop/cloud.aws_ops/pull/81).
- roles/enable_cloudtrail_encryption_with_kms - fix incorrect fact name for retrieved trail info and provide `s3_key_prefix` default so it doesn't error if not present (https://github.com/redhat-cop/cloud.aws_ops/pull/86).

New Roles
---------

- awsconfig_apigateway_with_lambda_integration - A role to create/delete an API gateway with lambda function integration.
- backup_create_plan - A role to create a backup plan and optionally a vault.
- backup_select_resources - A role to configure backups for selected resources.
- clone_on_prem_vm - A role to clone an existing on prem VM using the KVM hypervisor.
- create_rds_global_cluster - A role to create an Amazon Aurora global cluster with two different region rds clusters.
- deploy_flask_app - Deploy flask app in AWS.
- import_image_and_run_aws_instance - A role that imports a local .raw image into an Amazon Machine Image (AMI) and run an AWS EC2 instance.
- manage_transit_gateway - Creation/Deletion of transit gateway with vpc/vpn attachment
- manage_vpc_peering - A role to create, delete and accept existing VPC peering connections.
- move_objects_between_buckets - A role to move objects from one S3 Bucket to another.

v1.0.3
======

Release Summary
---------------

This release updates the documentation for the collection.

v1.0.2
======

Minor Changes
-------------

- various playbooks - minor linting fixes (https://github.com/ansible-collections/cloud.aws_ops/pull/21).
- various plugins - formating using black (https://github.com/ansible-collections/cloud.aws_ops/pull/21).
- various roles - minor linting fixes (https://github.com/ansible-collections/cloud.aws_ops/pull/21).
- various tests - minor linting fixes (https://github.com/ansible-collections/cloud.aws_ops/pull/21).

v1.0.1
======

Release Summary
---------------

Re-release 1.0.0 with updated README and generated CHNAGELOG, initial release of the collection
