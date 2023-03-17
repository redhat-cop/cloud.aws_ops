# cloud.aws_ops roles/playbooks to demo Ansible on AWS

This repository hosts the `cloud.aws_ops` Ansible Collection.

The collection includes a variety of Ansible roles and playbooks to help automate the management of resources on AWS.

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

### Requirements

The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [community.aws](https://github.com/ansible-collections/amazon.aws) collections MUST be installed in order for this collection to work.


### Installation
Clone the collection repository.

```shell
  mkdir -p ~/.ansible/collections/ansible_collections/cloud/aws_ops
  cd ~/.ansible/collections/ansible_collections/cloud/aws_ops
  git clone https://github.com/redhat-cop/cloud.aws_ops .
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

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.
