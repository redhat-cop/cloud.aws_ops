# AWS Operations Collection for Ansible
The Ansible AWS Operations collection includes a variety of Ansible content to help automate, manage, and streamline common operational tasks within AWS environments. This collection is maintained by the Red Hat Communities of Practice.

## Contents

- [Description](#description)
- [Requirements](#requirements)
  - [Ansible Version Compatibility](#ansible-version-compatibility)
  - [Python Version Compatibility](#python-version-compatibility)
  - [AWS Version Compatibility](#aws-version-compatibility)
- [Included Content](#included-content)
- [Installation](#installation)
  - [Installing Dependencies](#installing-dependencies)
- [Use Cases](#use-cases)
- [Testing](#testing)
- [Contributing to This Collection](#contributing-to-this-collection)
- [Support](#support)
- [Release Notes](#release-notes)
- [Related Information](#related-information)
- [Code of Conduct](#code-of-conduct)
- [License Information](#license-information)

## Description

The primary purpose of this collection is to simplify and streamline AWS operations through automation. By leveraging this collection, organizations can reduce manual operational effort, minimize errors, and ensure consistent approaches to managing AWS infrastructure. This leads to faster deployments, better security posture, and more reliable infrastructure management.

## Requirements

### Ansible Version Compatibility

<!--start requires_ansible-->
This collection has been tested against the following Ansible versions: **>=2.17.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

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
[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/aws_setup_credentials/README.md)|A role to define credentials for AWS modules.
[cloud.aws_ops.awsconfig_apigateway_with_lambda_integration](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/awsconfig_apigateway_with_lambda_integration/README.md)|A role to create/delete an API Gateway with Lambda function integration.
[cloud.aws_ops.awsconfig_detach_and_delete_internet_gateway](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/awsconfig_detach_and_delete_internet_gateway/README.md)|A role to detach and delete the internet gateway you specify from a virtual private cloud.
[cloud.aws_ops.awsconfig_multiregion_cloudtrail](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/awsconfig_multiregion_cloudtrail/README.md)|A role to create/delete a trail for multiple regions.
[cloud.aws_ops.backup_create_plan](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/backup_create_plan/README.md)|A role to create an AWS Backup plan.
[cloud.aws_ops.backup_select_resources](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/backup_select_resources/README.md)|A role to select resources to back up with an existing backup plan.
[cloud.aws_ops.clone_on_prem_vm](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/clone_on_prem_vm/README.md)|A role to clone an existing on-premises VM using the KVM hypervisor.
[cloud.aws_ops.create_rds_global_cluster](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/create_rds_global_cluster/README.md)|A role to create/delete Aurora global cluster with a primary cluster and a replica cluster in different regions.
[cloud.aws_ops.customized_ami](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/customized_ami/README.md)|A role to manage custom AMIs on AWS.
[cloud.aws_ops.deploy_flask_app](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/deploy_flask_app/README.md)|A role to deploy a Flask web application on AWS.
[cloud.aws_ops.ec2_instance_terminate_by_tag](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/ec2_instance_terminate_by_tag/README.md)|A role to terminate EC2 instances based on a specific tag you specify.
[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/ec2_networking_resources/README.md)|A role to manage EC2 networking resources.
[cloud.aws_ops.enable_cloudtrail_encryption_with_kms](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/enable_cloudtrail_encryption_with_kms/README.md)|A role to encrypt an AWS CloudTrail trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.
[cloud.aws_ops.import_image_and_run_aws_instance](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/import_image_and_run_aws_instance/README.md)|A role that imports a local .raw image into an Amazon Machine Image (AMI) and runs an AWS EC2 instance.
[cloud.aws_ops.manage_ec2_instance](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/manage_ec2_instance/README.md)|A role to manage EC2 instance lifecycle operations.
[cloud.aws_ops.manage_transit_gateway](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/manage_transit_gateway/README.md)|A role to create/delete transit gateway with VPC and VPN attachments.
[cloud.aws_ops.manage_vpc_peering](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/manage_vpc_peering/README.md)|A role to create, delete, and accept existing VPC peering connections.
[cloud.aws_ops.move_objects_between_buckets](https://github.com/redhat-cop/cloud.aws_ops/blob/main/roles/move_objects_between_buckets/README.md)|A role to move objects from one S3 bucket to another bucket.

### Playbooks

Name | Description
--- | ---
[cloud.aws_ops.eda](https://github.com/redhat-cop/cloud.aws_ops/blob/main/playbooks/README.md)|A set of playbooks to restore AWS CloudTrail configurations, created for use with Event-Driven Ansible rulebooks.
[cloud.aws_ops.webapp](https://github.com/redhat-cop/cloud.aws_ops/blob/main/playbooks/webapp/README.md)|A set of playbooks to create, delete, or migrate a web application on AWS.
[cloud.aws_ops.upload_file_to_s3](https://github.com/redhat-cop/cloud.aws_ops/blob/main/playbooks/UPLOAD_FILE_TO_S3.md)|A playbook to upload a local file to S3.
[cloud.aws_ops.move_vm_from_on_prem_to_aws](https://github.com/redhat-cop/cloud.aws_ops/blob/main/playbooks/move_vm_from_on_prem_to_aws/README.md)|A playbook to migrate an existing on-premises VM running on KVM hypervisor to AWS.

### Rulebooks

Name | Description
--- | ---
[cloud.aws_ops.aws_manage_cloudtrail_encryption](https://github.com/redhat-cop/cloud.aws_ops/blob/main/extensions/eda/AWS_MANAGE_CLOUDTRAIL_ENCRYPTION.md)|An Event-Driven Ansible rulebook to ensure that an existing encrypted AWS CloudTrail trail will not be deleted or have its encryption removed.

### Modules

Name | Description
--- | ---
[cloud.aws_ops.validate_network_acls](https://github.com/redhat-cop/cloud.aws_ops/blob/main/plugins/modules/validate_network_acls.py)|Validates network ACL configurations for connectivity between AWS resources.
[cloud.aws_ops.validate_route_tables](https://github.com/redhat-cop/cloud.aws_ops/blob/main/plugins/modules/validate_route_tables.py)|Validates route table configurations for connectivity between AWS resources.
[cloud.aws_ops.validate_security_group_rules](https://github.com/redhat-cop/cloud.aws_ops/blob/main/plugins/modules/validate_security_group_rules.py)|Validates security group rules for connectivity between AWS resources.

<!--end collection content-->

## Installation

The cloud.aws_ops collection can be installed with the Ansible Galaxy command-line tool:

```shell
ansible-galaxy collection install cloud.aws_ops
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: cloud.aws_ops
```

Note that if you install any collections from Ansible Galaxy, they will not be upgraded automatically when you upgrade the Ansible package.
To upgrade the collection to the latest available version, run the following command:

```shell
ansible-galaxy collection install cloud.aws_ops --upgrade
```

A specific version of the collection can be installed by using the `version` keyword in the `requirements.yml` file:

```yaml
---
collections:
  - name: cloud.aws_ops
    version: 5.0.0
```

or using the `ansible-galaxy` command as follows:

```shell
ansible-galaxy collection install cloud.aws_ops:==5.0.0
```

To consume this Validated Content from Automation Hub, please ensure that you add the following lines to your ansible.cfg file:

```ini
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```

The token can be obtained from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

### Installing Dependencies

The collection dependencies are not installed by `ansible-galaxy` by default. They must be installed separately:

```shell
ansible-galaxy collection install amazon.aws:>=5.1.0
ansible-galaxy collection install community.aws:>=5.0.0
ansible-galaxy collection install amazon.cloud:>=0.4.0
ansible-galaxy collection install community.libvirt:>=1.2.0
```

The Python module dependencies can be installed using pip:

```shell
pip install boto3>=1.26.0 botocore>=1.29.0
```

Refer to the following for more details:
* [Using Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

## Use Cases

You can call roles by their Fully Qualified Collection Name (FQCN), such as `cloud.aws_ops.enable_cloudtrail_encryption_with_kms`, or by their short name if you list the `cloud.aws_ops` collection in the playbook's `collections` keyword:

```yaml
---
- hosts: localhost
  gather_facts: false
  connection: local

  tasks:
    - name: Restore encryption to an existing AWS CloudTrail trail
      ansible.builtin.include_role:
        name: cloud.aws_ops.enable_cloudtrail_encryption_with_kms
      vars:
        enable_cloudtrail_encryption_with_kms_trail_name: "{{ cloudtrail_name }}"
        enable_cloudtrail_encryption_with_kms_kms_key_id: "{{ kms_alias }}"

    - name: Create VPC peering connection
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        manage_vpc_peering_operation: create
        manage_vpc_peering_vpc_id: "{{ vpc_id_1 }}"
        manage_vpc_peering_peer_vpc_id: "{{ vpc_id_2 }}"
```

If upgrading older playbooks which were built prior to Ansible 2.10 and this collection's existence, you can also define `collections` in your play and refer to this collection's roles as you did in Ansible 2.9 and below, as in this example:

```yaml
---
- hosts: localhost
  gather_facts: false
  connection: local

  collections:
    - cloud.aws_ops

  tasks:
    - name: Create AWS Backup plan
      ansible.builtin.include_role:
        name: backup_create_plan
      vars:
        backup_create_plan_name: "{{ backup_plan_name }}"
        backup_create_plan_rules: "{{ backup_rules }}"
```

For migrating VMs from on-premises to AWS:

```yaml
---
- hosts: all
  tasks:
    - name: Clone on-premises VM
      ansible.builtin.import_role:
        name: cloud.aws_ops.clone_on_prem_vm
      vars:
        clone_on_prem_vm_source_vm_name: "{{ source_vm_name }}"
        clone_on_prem_vm_image_name: "{{ image_name }}"
        clone_on_prem_vm_uri: "{{ uri }}"
        clone_on_prem_vm_local_image_path: "{{ local_image_path }}"
        clone_on_prem_vm_overwrite: "{{ overwrite }}"
      delegate_to: kvm

    - name: Import image and run AWS instance
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

This collection is tested using GitHub Actions. To learn more about testing, refer to [CI.md](https://github.com/redhat-cop/cloud.aws_ops/blob/main/CI.md).

## Contributing to This Collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [AWS Operations collection repository](https://github.com/redhat-cop/cloud.aws_ops).

If you want to develop new content for this collection or improve what's already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

See [CONTRIBUTING.md](https://github.com/redhat-cop/cloud.aws_ops/blob/main/CONTRIBUTING.md) for more details.

### More information about contributing

- [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) - Details on contributing to Ansible
- [Contributing to Collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections) - How to check out collection git repositories correctly

## Support

We announce releases and important changes through Ansible's [The Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn). Be sure you are [subscribed](https://eepurl.com/gZmiEP).

We take part in the global quarterly [Ansible Contributor Summit](https://github.com/ansible/community/wiki/Contributor-Summit) virtually or in-person. Track [The Bullhorn newsletter](https://eepurl.com/gZmiEP) and join us.

For more information about communication, refer to the [Ansible Communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

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
