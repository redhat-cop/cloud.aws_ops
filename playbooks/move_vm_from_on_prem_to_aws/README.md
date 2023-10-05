# cloud.aws_ops.move_vm_from_on_prem_to_aws playbooks

A playbook to migrate an existing on prem VM running on KVM hypervisor to AWS.

## Requirements

**qemu** and **qemu-img** packages installed.

The ``cloud.gcp_ops.clone_one_prem_vm`` requires privilege escalation because the .qcow2 file created by ``virt-clone`` is owned by root and ``qemu-img convert`` requires access to convert it to .raw.

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

## Playbook Variables

* **kvm_host** (dict): Information about the host running the KVM hypervisr that are dynamically added to the inventory.
    * **name**: This is a user-defined name for the host you are adding to the inventory.
    * **ansible_host**: This variable specifies the hostname or IP address of the host you are adding to the inventory.
    * **ansible_user**: This variable specifies the SSH username that Ansible should use when connecting to the host.
    * **ansible_ssh_private_key_file** This variable specifies the path to the SSH private key file that Ansible should use for authentication when connecting to the host.
    * **groups** This variable enabled you to assign the newly added host to one or more groups in the inventory.

### Needed for the cloud.aws_ops.clone_on_prem_vm role

* **clone_on_prem_vm_source_vm_name** (str): (Required) The name of the on-prem VM you want to clone.
* **clone_on_prem_vm_image_name** (str): (Optional) The name you want to call the cloned image. If not set, the **clone_on_prem_vm_source_vm_name** will be used with a _-clone_ suffix.
* **clone_on_prem_vm_uri** (str): (Optional) Libvirt connection uri. Default: "qemu:///system".
* **clone_on_prem_vm_overwrite** (bool): (Optional) Whether to overwrite or not an already existing on prem VM clone. Default: true.
* **clone_on_prem_vm_local_image_path** (str): (Optional) The path where you would like to save the image. If the path does not exists on localhost, the role will create it. If this parameter is not set, the role will save the image in a _~/tmp_ folder.

### Needed for the cloud.aws_ops.import_image_and_run_aws_instance role

* **aws_access_key** (str): (Required) AWS access key ID for user account with the above permissions
* **aws_secret_key** (str): (Required) AWS secret access key for user account with the above permissions
* **aws_region** (str): (Required) AWS region in which to run the EC2 instance
* **security_token** (str): (Optional) Security token for AWS session authentication
* **import_image_and_run_aws_instance_bucket_name** (str): (Required) The name of the S3 bucket name where you want to upload the .raw image. It must exist in the region the instance is created.
* **import_image_and_run_aws_instance_import_image_task_name** (str): (Required) The  name you want to assign to the AWS EC2 import image task.
* **import_image_and_run_aws_instance_image_path** (str): (Required) The path where the .raw image is stored.
* **import_image_and_run_aws_instance_instance_name** (str): (Required) The name of the EC2 instance you want to create using the imported AMI.
* **import_image_and_run_aws_instance_instance_type** (str): (Optional) The EC2 instance type you want to use. Default: "t2.micro".
* **import_image_and_run_aws_instances_keypair_name** (str): (Optional) The name of the SSH access key to assign to the EC2 instance. It must exist in the region the instance is created. If not set, your default AWS account keypair will be used.
* **import_image_and_run_aws_instance_security_groups** (list): (Optional) A list of security group IDs or names to assiciate to the EC2 instance.
* **import_image_and_run_aws_instance_vpc_subnet_id** (str): (Optional) The subnet ID in which to launch the EC2 instance instance (VPC). If none is provided, M(amazon.aws.ec2_instance) will chose the default zone of the default VPC.
* **import_image_and_run_aws_instance_volumes** (dict): (Optional) A dictionary of a block device mappings, by default this will always use the AMI root device so the **import_image_and_run_aws_instance_volumes** option is primarily for adding more storage. A mapping contains the (optional) keys:
    * **device_name** (str): The device name (for example, /dev/sdh or xvdh).
    * **ebs** (dict): Parameters used to automatically set up EBS volumes when the instance is launched.
        * **volume_type** (str): The volume type. Valid Values: standard, io1, io2, gp2, sc1, st1, gp3.
        * **volume_size** (int): The size of the volume, in GiBs.
        * **kms_key_id** (str): Identifier (key ID, key alias, ID ARN, or alias ARN) for a customer managed CMK under which the EBS volume is encrypted.
        * **iops** (str): The number of I/O operations per second (IOPS). For gp3, io1, and io2 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
        * **delete_on_termination_** (bool): Indicates whether the EBS volume is deleted on instance termination.

## Example Usage

Create a `credentials.yaml` file with the folling contents:

```yaml
aws_access_key: "xxxxxxxxxxxxxxxxxxxx"
aws_secret_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aws_region: "us-east-1"
```

All the variables defined in section ``Playbook Variables`` can be defined inside the ``vars/main.yml`` file.

Run the playbook:

```shell
ansible-playbook cloud.gcp_ops.move_vm_from_on_prem_to_aws -e "@credentials.yaml"
```
