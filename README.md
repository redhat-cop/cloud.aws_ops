# cloud.aws_ops roles/playbook to demo ansible on aws

This repository hosts the `cloud.aws_ops` Ansible Collection.

The collection includes a variety of Ansible roles and playbook to help automate the management of resources on AWS.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.11.0**.

## Included content

Click on the name of a role to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[cloud.aws_ops.aws_setup_credentials](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/aws_setup_credentials/README.md)|A role to define credentials for aws modules.
[cloud.aws_ops.awsconfig_detach_and_delete_internet_gateway](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/awsconfig_detach_and_delete_internet_gateway/README.md)|A role to detach and delete the internet gateway you specify from virtual private cloud.
[cloud.aws_ops.awsconfig_multiregion_cloudtrail](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/awsconfig_multiregion_cloudtrail/README.md)|A role to create/delete a Trail for multiple regions.
[cloud.aws_ops.customized_ami](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/customized_ami/README.md)|A role to manage custom AMIs on AWS.
[cloud.aws_ops.ec2_instance_terminate_by_tag](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/ec2_instance_terminate_by_tag/README.md)|A role to terminate the EC2 instances based on a specific tag you specify.
[cloud.aws_ops.enable_cloudtrail_encryption_with_kms](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/enable_cloudtrail_encryption_with_kms/README.md)|A role to encrypt an AWS CloudTrail trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.


### Playbooks
Name | Description
--- | ---
cloud.aws_ops.webapp|A playbook to create a webapp on AWS.
<!--end collection content-->

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the amazon_roles collection, you need to install it with the Ansible Galaxy CLI:

    ansible-galaxy collection install cloud.cloud.aws_ops

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: cloud.aws_ops
    version: 1.0.0
```

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.
