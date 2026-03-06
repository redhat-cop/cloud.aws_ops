# cloud.aws_ops Validated Content Collection
The Ansible AWS Operations collection includes a variety of Ansible content to help automate, manage, and streamline common operational tasks within AWS environments. This collection is maintained by the [Red Hat Communities of Practice](https://github.com/redhat-cop).

## Contents

- [Description](#description)
- [Requirements](#requirements)
  - [Ansible Version Compatibility](#ansible-version-compatibility)
  - [Python Version Compatibility](#python-version-compatibility)
  - [AWS Version Compatibility](#aws-version-compatibility)
- [Included Content](#included-content)
  - [Roles](#roles)
  - [Playbooks](#playbooks)
  - [Rulebooks](#rulebooks)
  - [Modules](#modules)
- [Installation](#installation)
  - [Installing Dependencies](#installing-dependencies)
- [Use Cases](#use-cases)
- [Testing](#testing)
  - [Continuous Integration](#continuious-integration)
  - [Testing with ansible-test](#testing-with-ansible-test)
- [Contributing to This Collection](#contributing-to-this-collection)
- [Support](#support)
- [Release Notes](#release-notes)
- [Related Information](#related-information)
- [Code of Conduct](#code-of-conduct)
- [License Information](#license-information)

## Description

This collection is curated to provide users with a robust set of roles, playbooks, and rulebooks that simplify and streamline various AWS operations. By leveraging this collection, organizations can reduce manual operational effort, minimize errors, and ensure consistent approaches to managing AWS infrastructure. This leads to faster deployments, better security posture, and more reliable infrastructure management.

## Requirements

### Ansible Version Compatibility

This collection has been tested against the following Ansible versions: **>=2.17.0**.

### Python Version Compatibility

This collection requires Python 3.10+.

### AWS Version Compatibility

This collection requires the following collection dependencies:
- [amazon.aws](https://github.com/ansible-collections/amazon.aws) (>=5.1.0)
- [community.aws](https://github.com/ansible-collections/community.aws) (>=5.0.0)
- [amazon.cloud](https://github.com/ansible-collections/amazon.cloud) (>=0.4.0)
- [community.libvirt](https://github.com/ansible-collections/community.libvirt) (>=1.2.0)

For Event-Driven Ansible features, [ansible-rulebook](https://ansible.readthedocs.io/projects/rulebook/en/latest/) must be installed separately.

## Included Content

Click on the name of a role, playbook, or rulebook to view that content's documentation:

<!--start collection content-->
### Roles

Name | Description
--- | ---
[cloud.aws_ops.aws_setup_credentials](roles/aws_setup_credentials/README.md)|A role to define credentials for AWS modules.
[cloud.aws_ops.awsconfig_apigateway_with_lambda_integration](roles/awsconfig_apigateway_with_lambda_integration/README.md)|A role to create/delete an API Gateway with Lambda function integration.
[cloud.aws_ops.awsconfig_detach_and_delete_internet_gateway](roles/awsconfig_detach_and_delete_internet_gateway/README.md)|A role to detach and delete the internet gateway you specify from a virtual private cloud.
[cloud.aws_ops.awsconfig_multiregion_cloudtrail](roles/awsconfig_multiregion_cloudtrail/README.md)|A role to create/delete a trail for multiple regions.
[cloud.aws_ops.backup_create_plan](roles/backup_create_plan/README.md)|A role to create an AWS Backup plan.
[cloud.aws_ops.backup_select_resources](roles/backup_select_resources/README.md)|A role to select resources to back up with an existing backup plan.
[cloud.aws_ops.clone_on_prem_vm](roles/clone_on_prem_vm/README.md)|A role to clone an existing on-premises VM using the KVM hypervisor.
[cloud.aws_ops.create_rds_global_cluster](roles/create_rds_global_cluster/README.md)|A role to create/delete Aurora global cluster with a primary cluster and a replica cluster in different regions.
[cloud.aws_ops.customized_ami](roles/customized_ami/README.md)|A role to manage custom AMIs on AWS.
[cloud.aws_ops.deploy_flask_app](roles/deploy_flask_app/README.md)|A role to deploy a Flask web application on AWS.
[cloud.aws_ops.ec2_instance_terminate_by_tag](roles/ec2_instance_terminate_by_tag/README.md)|A role to terminate EC2 instances based on a specific tag you specify.
[cloud.aws_ops.ec2_networking_resources](roles/ec2_networking_resources/README.md)|A role to manage EC2 networking resources.
[cloud.aws_ops.enable_cloudtrail_encryption_with_kms](roles/enable_cloudtrail_encryption_with_kms/README.md)|A role to encrypt an AWS CloudTrail trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.
[cloud.aws_ops.import_image_and_run_aws_instance](roles/import_image_and_run_aws_instance/README.md)|A role that imports a local .raw image into an Amazon Machine Image (AMI) and runs an AWS EC2 instance.
[cloud.aws_ops.manage_ec2_instance](roles/manage_ec2_instance/README.md)|A role to manage EC2 instance lifecycle operations.
[cloud.aws_ops.manage_transit_gateway](roles/manage_transit_gateway/README.md)|A role to create/delete transit gateway with VPC and VPN attachments.
[cloud.aws_ops.manage_vpc_peering](roles/manage_vpc_peering/README.md)|A role to create, delete, and accept existing VPC peering connections.
[cloud.aws_ops.move_objects_between_buckets](roles/move_objects_between_buckets/README.md)|A role to move objects from one S3 bucket to another bucket.

### Playbooks

Name | Description
--- | ---
[cloud.aws_ops.eda](playbooks/README.md)|A set of playbooks to restore AWS CloudTrail configurations, created for use with Event-Driven Ansible rulebooks.
[cloud.aws_ops.webapp](playbooks/webapp/README.md)|A set of playbooks to create, delete, or migrate a web application on AWS.
[cloud.aws_ops.upload_file_to_s3](playbooks/UPLOAD_FILE_TO_S3.md)|A playbook to upload a local file to S3.
[cloud.aws_ops.move_vm_from_on_prem_to_aws](playbooks/move_vm_from_on_prem_to_aws/README.md)|A playbook to migrate an existing on-premises VM running on KVM hypervisor to AWS.

### Rulebooks

Name | Description
--- | ---
[cloud.aws_ops.aws_manage_cloudtrail_encryption](extensions/eda/AWS_MANAGE_CLOUDTRAIL_ENCRYPTION.md)|An Event-Driven Ansible rulebook to ensure that an existing encrypted AWS CloudTrail trail will not be deleted or have its encryption removed.

### Modules

Name | Description
--- | ---
[cloud.aws_ops.validate_network_acls](plugins/modules/validate_network_acls.py)|Validates network ACL configurations for connectivity between AWS resources.
[cloud.aws_ops.validate_route_tables](plugins/modules/validate_route_tables.py)|Validates route table configurations for connectivity between AWS resources.
[cloud.aws_ops.validate_security_group_rules](plugins/modules/validate_security_group_rules.py)|Validates security group rules for connectivity between AWS resources.

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

Refer to the following for more details:
* [Using Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

## Use Cases

You can call roles by their Fully Qualified Collection Name (FQCN), such as `cloud.aws_ops.enable_cloudtrail_encryption_with_kms`:

```yaml
  # The following example restores encryption to an existing AWS Cloudtrail trail using the enable_cloudtrail_encryption_with_kms role
  - hosts: all
    tasks:
      - name: Include 'enable_cloudtrail_encryption_with_kms' role
        ansible.builtin.include_role:
          name: cloud.aws_ops.enable_cloudtrail_encryption_with_kms
        vars:
          enable_cloudtrail_encryption_with_kms_trail_name: "{{ cloudtrail_name }}"
          enable_cloudtrail_encryption_with_kms_kms_key_id: "{{ kms_alias }}"

  # The following example uses the ``cloud.aws_ops.clone_on_prem_vm`` role to clone an existing VM on prem using the KVM hypervisor and the ``cloud.aws_ops.import_image_and_run_aws_instance`` role to import a local .raw image into an Amazon machine image (AMI) and run an AWS EC2 instance.

  - hosts: all
    tasks:
    - name: Import 'cloud.aws_ops.clone_on_prem_vm' role
      ansible.builtin.import_role:
        name: cloud.aws_ops.clone_on_prem_vm
      vars:
        clone_on_prem_vm_source_vm_name: "{{ source_vm_name }}"
        clone_on_prem_vm_image_name: "{{ image_name }}"
        clone_on_prem_vm_uri: "{{ uri }}"
        clone_on_prem_vm_local_image_path: "{{ local_image_path }}"
        clone_on_prem_vm_overwrite: "{{ overwrite }}"
      delegate_to: kvm

    - name: Import 'cloud.aws_ops.import_image_and_run_aws_instance' role
      ansible.builtin.import_role:
        name: cloud.aws_ops.import_image_and_run_aws_instance
      vars:
        import_image_and_run_aws_instance_bucket_name: "{{ bucket_name }}"
        import_image_and_run_aws_instance_image_path: "{{ raw_image_path }}"
        import_image_and_run_aws_instance_instance_name: "{{ instance_name }}"
        import_image_and_run_aws_instance_instance_type: "{{ instance_type }}"
        import_image_and_run_aws_instance_import_image_task_name: "{{ import_image_task_name }}"
        import_image_and_run_aws_instance_keypair_name: "{{ keypair_name }}"
```

For documentation on how to use individual roles and other content included in this collection, please see the links in the [Included Content](#included-content) section.

## Testing

### Continuious Integration

This collection is tested using GitHub Actions. To learn more about the continuous integration process, refer to [CI.md](./CI.md).

### Testing with `ansible-test`

The `tests` directory contains configuration for running sanity and integration tests using [`ansible-test`](https://docs.ansible.com/ansible/latest/dev_guide/testing_integration.html).

You can run the collection's test suites with the commands:

```shell
# Run sanity tests
ansible-test sanity

# Run integration tests (requires AWS credentials)
ansible-test integration [target]
```

Before running integration tests, you must configure AWS credentials:

```shell
# Using the "default" profile on AWS
aws configure set aws_access_key_id your-access-key
aws configure set aws_secret_access_key your-secret-key
aws configure set region us-east-1
```

The collection also uses `tox` for linting. Assuming this repository is checked out in the proper structure (e.g., `collections_root/ansible_collections/cloud/aws_ops/`), run:

```shell
# Run all linters (black, flake8, yamllint)
tox -e linters

# Run ansible-lint separately
tox -e ansible-lint

# Run black formatter
tox -e black
```

## Contributing to This Collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [AWS Operations collection repository](https://github.com/redhat-cop/cloud.aws_ops).

If you want to develop new content for this collection or improve what's already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

See [CONTRIBUTING.md](https://github.com/redhat-cop/cloud.aws_ops/blob/main/CONTRIBUTING.md) for more details.

### More information about contributing

- [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) - Details on contributing to Ansible
- [Contributing to Collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections) - How to check out collection git repositories correctly

## Support

- We announce releases and important changes through Ansible's [The Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn).
- We take part in the global quarterly [Ansible Contributor Summit](https://github.com/ansible/community/wiki/Contributor-Summit) virtually or in-person.
- For more information about communication, refer to the [Ansible Communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).
For the latest supported versions, refer to the release notes below.

If you encounter issues or have questions, you can submit a support request through the following channels:
 - GitHub Issues: Report bugs, request features, or ask questions by opening an issue in the [GitHub repository](https://github.com/redhat-cop/cloud.aws_ops/).
 - Ansible Community: Engage with the Ansible community on the Ansible Project Mailing List or [Ansible Forum](https://forum.ansible.com/g/AWS).

## Release Notes

See the [raw generated changelog](https://github.com/redhat-cop/cloud.aws_ops/blob/main/CHANGELOG.rst).

## Related Information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Ansible Rulebook documentation](https://ansible.readthedocs.io/projects/rulebook/en/stable/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.

## License Information

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
