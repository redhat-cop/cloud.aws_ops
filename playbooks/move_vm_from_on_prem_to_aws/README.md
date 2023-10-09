# cloud.aws_ops.move_vm_from_on_prem_to_aws playbooks

A playbook to migrate an existing on prem VM running on KVM hypervisor to AWS.

## Requirements

This playbook uses the ``cloud.aws_ops.clone_on_prem_vm`` role to clone an existing VM on prem using the KVM hypervisor and the ``cloud.aws_ops.import_image_and_run_aws_instance`` role to import a local .raw image into an Amazon machine image (AMI) and run an AWS EC2 instance. For a complete list of requirements, see [clone_on_prem_vm](../clone_on_prem_vm/README.md#Requirements) and [import_image_and_run_aws_instance](../roles/import_image_and_run_aws_instance/REAME.md#Requirements), respectively.


## Playbook Variables

For a fullo list of accepted variables see: [clone_on_prem_vm](../clone_on_prem_vm/README.md#Role-Variables) and respectively [import_image_and_run_aws_instance](../roles/import_image_and_run_aws_instance/REAME.md#Role-Variables).

## Example Usage

Create a `credentials.yml` file with the folling contents:

```yaml
aws_access_key: "xxxxxxxxxxxxxxxxxxxx"
aws_secret_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aws_region: "us-east-1"
```

Create an `inventory.yml` file with information about the host running the KVM hypervisor.

```yaml
---
all:
  hosts:
    kvm:
      ansible_host: myhost
      ansible_user: myuser
      ansible_ssh_private_key_file: /path/to/private_key
      groups: mygroup
```

All the variables defined in section ``Playbook Variables`` can be defined inside the ``vars/main.yml`` file.

Run the playbook:

```shell
ansible-playbook cloud.gcp_ops.move_vm_from_on_prem_to_aws -e "@credentials.yml - i inventory.yml"
```
