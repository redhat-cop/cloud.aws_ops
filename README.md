# cloud.aws_ops Validated Content Collection

This repository hosts the `cloud.aws_ops` Ansible Collection.

## Description

This collection is curated to provide users with a robust set of roles, playbooks, and rulebooks that simplify and streamline various AWS operations.

## Requirements

The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [community.aws](https://github.com/ansible-collections/amazon.aws) collections MUST be installed in order for this collection to work.

To run rulebooks, [ansible-rulebook](https://ansible.readthedocs.io/projects/rulebook/en/latest/) must be installed.

<!--start requires_ansible-->
### Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.15.0**.

### Included content

Click on the name of a role, playbook, or rulebook to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[cloud.aws_ops.aws_setup_credentials](roles/aws_setup_credentials/README.md)|A role to define credentials for aws modules.
[cloud.aws_ops.awsconfig_detach_and_delete_internet_gateway](roles/awsconfig_detach_and_delete_internet_gateway/README.md)|A role to detach and delete the internet gateway you specify from virtual private cloud.
[cloud.aws_ops.awsconfig_multiregion_cloudtrail](roles/awsconfig_multiregion_cloudtrail/README.md)|A role to create/delete a Trail for multiple regions.
[cloud.aws_ops.backup_create_plan](roles/backup_create_plan/README.md)|A role to create an AWS backup plan.
[cloud.aws_ops.backup_select_resources](roles/backup_select_resources/README.md)|A role to select resources to back up with an existing backup plan.
[cloud.aws_ops.customized_ami](roles/customized_ami/README.md)|A role to manage custom AMIs on AWS.
[cloud.aws_ops.ec2_instance_terminate_by_tag](roles/ec2_instance_terminate_by_tag/README.md)|A role to terminate the EC2 instances based on a specific tag you specify.
[cloud.aws_ops.enable_cloudtrail_encryption_with_kms](roles/enable_cloudtrail_encryption_with_kms/README.md)|A role to encrypt an AWS CloudTrail trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.
[cloud.aws_ops.manage_vpc_peering](roles/manage_vpc_peering/README.md)|A role to create, delete and accept existing VPC peering connections.
[cloud.aws_ops.move_objects_between_buckets](roles/move_objects_between_buckets/README.md)|A role to move objects from one bucket to another bucket.
[cloud.aws_ops.awsconfig_apigateway_with_lambda_integration](roles/awsconfig_apigateway_with_lambda_integration/README.md)|A role to create/delete an API gateway with lambda function integration.
[cloud.aws_ops.manage_transit_gateway](roles/manage_transit_gateway/README.md)|A role to create/delete transit_gateway with vpc and vpn attachments.
[cloud.aws_ops.deploy_flask_app](roles/deploy_flask_app/README.md)|A role to deploy a flask web application on AWS.
[cloud.aws_ops.create_rds_global_cluster](roles/create_rds_global_cluster/README.md)|A role to create, delete aurora global cluster with a primary cluster and a replica cluster in different regions.
[cloud.aws_ops.clone_on_prem_vm](roles/clone_on_prem_vm/README.md)|A role to clone an existing on prem VM using the KVM hypervisor.
[cloud.aws_ops.import_image_and_run_aws_instance](roles/import_image_and_run_aws_instance/README.md)|A role that imports a local .raw image into an Amazon Machine Image (AMI) and run an AWS EC2 instance.

### Playbooks
Name | Description
--- | ---
[cloud.aws_ops.eda](playbooks/README.md)|A set of playbooks to restore AWS Cloudtrail configurations, created for use with the [cloud.aws_manage_cloudtrail_encryption rulebook](extensions/eda/AWS_MANAGE_CLOUDTRAIL_ENCRYPTION.md).
[cloud.aws_ops.webapp](playbooks/webapp/README.md)|A set of playbooks to create, delete, or migrate a webapp on AWS.
[cloud.aws_ops.upload_file_to_s3](playbooks/UPLOAD_FILE_TO_S3.md)|A playbook to upload a local file to S3.
[cloud.aws_ops.move_vm_from_on_prem_to_aws](playbooks/move_vm_from_on_prem_to_aws/README.md)|A playbook to migrate an existing on prem VM running on KVM hypervisor to AWS.

### Rulebooks
Name | Description
--- | ---
[cloud.aws_ops.aws_manage_cloudtrail_encryption](extensions/eda/AWS_MANAGE_CLOUDTRAIL_ENCRYPTION.md)|An Event-Driven Ansible rulebook to ensure that an existing encrypted AWS Cloudtrail trail will not be deleted or have its encryption removed.
<!--end collection content-->

## Installation

To consume this Validated Content from Automation Hub, please ensure that you add the following lines to your ansible.cfg file.

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
The token can be obtained from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

Once the above steps are done, you can run the following command to install the collection.

```
ansible-galaxy collection install cloud.aws_ops
```

## Use Cases

Once installed, you can reference the cloud.aws_ops collection content by its fully qualified collection name (FQCN), for example:

```yaml
  - hosts: all
    tasks:
      - name: Include 'enable_cloudtrail_encryption_with_kms' role
        ansible.builtin.include_role:
          name: cloud.aws_ops.enable_cloudtrail_encryption_with_kms
        vars:
          enable_cloudtrail_encryption_with_kms_trail_name: "{{ cloudtrail_name }}"
          enable_cloudtrail_encryption_with_kms_kms_key_id: "{{ kms_alias }}"
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.

## Testing and Development

The project uses `ansible-lint` and `black`.
Assuming this repository is checked out in the proper structure,
e.g. `collections_root/ansible_collections/cloud/aws_ops/`, run:

```shell
  tox -e linters
```

Sanity and unit tests are run as normal:

```shell
  ansible-test sanity
```

If you want to run cloud integration tests, ensure you log in to the cloud:

```shell
# using the "default" profile on AWS
  aws configure set aws_access_key_id     my-access-key
  aws configure set aws_secret_access_key my-secret-key
  aws configure set region                eu-north-1

  ansible-test integration [target]
```

This collection is tested using GitHub Actions. To know more about CI, refer to [CI.md](https://github.com/https://github.com/redhat-cop/cloud.aws_ops/blob/main/CI.md).

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.

## Support

You can also join us on:

- Libera.Chat IRC - the ``#ansible-aws`` [irc.libera.chat](https://libera.chat/) channel

## Release Notes

See the [raw generated changelog](https://github.com/redhat-cop/cloud.aws_ops/blob/main/CHANGELOG.rst).


## Related Information

 - [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html).
 -  [Ansible Rulebook documentation](https://ansible.readthedocs.io/projects/rulebook/en/stable/index.html).
 - [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.
