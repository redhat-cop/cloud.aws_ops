import_image_and_run_aws_instance
=================================

A role that imports a local .raw image into an Amazon Machine Image (AMI) and run an AWS EC2 instance.

Requirements
------------

VM Import requires a role to perform certain operations on your behalf. You must create a service role named vmimport with a trust relationship policy document that allows VM Import to assume the role, and you must attach an IAM policy to the role.

AWS User Account with the following permissions:
* s3:GetBucketLocation
* s3:GetObject
* s3:ListBucket
* s3:GetBucketLocation
* s3:GetObject
* s3:ListBucket
* s3:PutObject
* s3:GetBucketAcl
* ec2:ModifySnapshotAttribute
* ec2:CopySnapshot
* ec2:RegisterImage
* ec2:Describe*
* ec2:RunInstances

(Optional) To import resources encrypted using an AWS KMS key from AWS Key Management Service, add the following permissions:
* kms:CreateGrant
* kms:Decrypt
* kms:DescribeKey
* kms:Encrypt
* kms:GenerateDataKey*
* kms:ReEncrypt*

Role Variables
--------------

* **import_image_and_run_aws_instance_import_image_task_name**: (Required) The name you want to assign to the AWS EC2 import image task.
* **import_image_and_run_aws_instance_bucket_name**: (Required) The name of the S3 bucket name where you want to upload the .raw image.
* **import_image_and_run_aws_instance_image_path**: (Required) The path where the .raw image is stored.
* **import_image_and_run_aws_instance_instance_name**: (Required) The name of the EC2 instance you want to create using the imported AMI.
* **import_image_and_run_aws_instance_instance_type**: The EC2 instance type you want to use. Default: "t2.micro".
* **import_image_and_run_aws_instances_keypair_name**: The name of the SSH access key to assign to the EC2 instance. It must exist in the region the instance is created. If not set, your default AWS account keypair will be used.
* **import_image_and_run_aws_instance_security_groups**: A list of security group IDs or names to associate to the EC2 instance.
* **import_image_and_run_aws_instance_vpc_subnet_id**: The subnet ID in which to launch the EC2 instance (VPC). If none is provided, M(amazon.aws.ec2_instance) will choose the default zone of the default VPC.
* **import_image_and_run_aws_instance_volumes** (dict): (Optional) A dictionary of a block device mappings, by default this will always use the AMI root device so the **instance_volumes** option is primarily for adding more storage. A mapping contains the (optional) keys:
    * **device_name** (str): The device name (for example, /dev/sdh or xvdh).
    * **ebs** (dict): Parameters used to automatically set up EBS volumes when the instance is launched.
        * **volume_type** (str): The volume type. Valid Values: standard, io1, io2, gp2, sc1, st1, gp3.
        * **volume_size** (int): The size of the volume, in GiBs.
        * **kms_key_id** (str): Identifier (key ID, key alias, ID ARN, or alias ARN) for a customer managed CMK under which the EBS volume is encrypted.
        * **iops** (str): The number of I/O operations per second (IOPS). For gp3, io1, and io2 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
        * **delete_on_termination_** (bool): Indicates whether the EBS volume is deleted on instance termination.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------
This role can be used together with the [cloud.aws_ops.clone_on_prem_vm](../clone_on_prem_vm/README.md) role as shown below.

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

All the variables defined in section ``Playbook Variables`` can be defined inside the ``vars.yml`` file.

Create a ``playbook.yml`` file like this:

```
---
- hosts: localhost
   gather_facts: false

   tasks:
     - name: Import 'cloud.aws_ops.clone_on_prem_vm' role
       ansible.builtin.import_role:
         name: cloud.aws_ops.clone_on_prem_vm
       vars:
         clone_on_prem_vm_source_vm_name: "{{ clone_on_prem_vm_source_vm_name }}"
         clone_on_prem_vm_image_name: "{{ clone_on_prem_vm_image_name }}"
         clone_on_prem_vm_local_image_path: "{{ clone_on_prem_vm_local_image_path }}"
         clone_on_prem_vm_uri: "{{ clone_on_prem_vm_uri }}"
       delegate_to: kvm

     - name: Import 'cloud.aws_ops.import_image_and_run_aws_instance' role
       ansible.builtin.import_role:
         name: cloud.aws_ops.import_image_and_run_aws_instance
       vars:
         import_image_and_run_aws_instance_bucket_name: "{{ import_image_and_run_aws_instance_bucket_name }}"
         import_image_and_run_aws_instance_image_path: "{{ clone_on_prem_vm_raw_image_path }}"
         import_image_and_run_aws_instance_instance_name: "{{ import_image_and_run_aws_instance_instance_name }}"
         import_image_and_run_aws_instance_instance_type: "{{ import_image_and_run_aws_instance_instance_type }}"
         import_image_and_run_aws_instance_import_image_task_name: "{{ import_image_and_run_aws_instance_import_image_task_name }}"
         import_image_and_run_aws_instances_keypair_name: "{{ import_image_and_run_aws_instances_keypair_name }}"
         import_image_and_run_aws_instance_security_groups: "{{ import_image_and_run_aws_instance_security_groups }}"
         import_image_and_run_aws_instance_vpc_subnet_id: "{{ import_image_and_run_aws_instance_vpc_subnet_id }}"
         import_image_and_run_aws_instance_volumes: "{{ import_image_and_run_aws_instance_volumes }}"
```

Run the playbook:

```shell
ansible-playbook playbook.yml -i inventory.yml -e "@vars.yml"
```


License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
