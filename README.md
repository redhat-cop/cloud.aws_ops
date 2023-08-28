# cloud.aws_ops roles/playbooks to demo Ansible on AWS

This repository hosts the `cloud.aws_ops` Ansible Collection.

The collection includes a variety of Ansible roles and playbooks to help automate the management of resources on AWS.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.12.0**.

## Included content

Click on the name of a role to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[cloud.aws_ops.aws_setup_credentials](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/aws_setup_credentials/README.md)|A role to define credentials for aws modules.
[cloud.aws_ops.awsconfig_detach_and_delete_internet_gateway](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/awsconfig_detach_and_delete_internet_gateway/README.md)|A role to detach and delete the internet gateway you specify from virtual private cloud.
[cloud.aws_ops.awsconfig_multiregion_cloudtrail](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/awsconfig_multiregion_cloudtrail/README.md)|A role to create/delete a Trail for multiple regions.
[cloud.backup_create_plan](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/backup_create_plan/README.md)|A role to create an AWS backup plan.
[cloud.backup_select_resources](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/backup_create_plan/README.md)|A role to select resources to back up with an existing backup plan.
[cloud.aws_ops.customized_ami](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/customized_ami/README.md)|A role to manage custom AMIs on AWS.
[cloud.aws_ops.ec2_instance_terminate_by_tag](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/ec2_instance_terminate_by_tag/README.md)|A role to terminate the EC2 instances based on a specific tag you specify.
[cloud.aws_ops.enable_cloudtrail_encryption_with_kms](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/enable_cloudtrail_encryption_with_kms/README.md)|A role to encrypt an AWS CloudTrail trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.
[cloud.aws_ops.manage_vpc_peering](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/manage_vpc_peering/README.md)|A role to create, delete and accept existing VPC peering connections.
[cloud.aws_ops.moving_objects_between_buckets](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/moving_objects_between_buckets/README.md)|A role to move objects from one bucket to another bucket.
[cloud.aws_ops.awsconfig_apigateway_with_lambda_integration](https://github.com/ansible-collections/cloud.aws_ops/blob/main/roles/awsconfig_apigateway_with_lambda_integration/README.md)|A role to create/delete an API gateway with lambda function integration.


### Playbooks
Name | Description
--- | ---
cloud.aws_ops.webapp|A playbook to create a webapp on AWS.
<!--end collection content-->

## Installation and Usage

### Requirements

The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [community.aws](https://github.com/ansible-collections/amazon.aws) collections MUST be installed in order for this collection to work.


### Installation

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

### Using this collection

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

### See Also

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.


## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.

### Testing and Development

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

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.
