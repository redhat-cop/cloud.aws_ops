# cloud.aws_ops.import_image_and_run_aws_instance playbooks

A playbook to migrate an existing on prem VM running on KVM hypervisor to AWS.

## Requirements

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

### Needed for the cloud.aws_ops.clone_on_prem_vm role

* **on_prem_source_vm_name** (str): (Required) The name of the on-prem VM you want to clone.
* **on_prem_vm_clone_name** (str): (Optional) The name you want to call the cloned image. If not set, the **on_prem_vm_clone_name** will be used with a _-clone_ suffix.
* **uri** (str): (Optional) Libvirt connection uri. Default: "qemu:///system".
* **overwrite_clone** (bool): (Optional) Weather to overwrite or not an already existing on prem VM clone. Default: true.

### Needed for the cloud.aws_ops.import_image_and_run_aws_instance role

* **aws_access_key** (str): (Required) AWS access key ID for user account with the above permissions
* **aws_secret_key** (str): (Required) AWS secret access key for user account with the above permissions
* **aws_region** (str): (Required) AWS region in which to run the EC2 instance
* **security_token** (str): (Optional) Security token for AWS session authentication
* **s3_bucket_name** (str): (Required) The name of the S3 bucket name where you want to upload the .raw image. It must exist in the region the instance is created.
* **import_task_name** (str): (Required) The  name you want to assign to the AWS EC2 import image task.
* **image_path** (str): (Required) The path where the .raw image is stored.
* **instance_name** (str): (Required) The name of the EC2 instance you want to create using the imported AMI.
* **instance_type** (str): (Optional) The EC2 instance type you want to use. Default: "t2.micro".
* **keypair_name** (str): (Optional) The name of the SSH access key to assign to the EC2 instance. It must exist in the region the instance is created. If not set, your default AWS account keypair will be used.
* **security_groups** (list): (Optional) A list of security group IDs or names to assiciate to the EC2 instance.
* **vpc_subnet_id** (str): (Optional) The subnet ID in which to launch the EC2 instance instance (VPC). If none is provided, M(amazon.aws.ec2_instance) will chose the default zone of the default VPC.
* **instance_volumes** (dict): (Optional) A dictionary of a block device mappings, by default this will always use the AMI root device so the **instance_volumes** option is primarily for adding more storage. A mapping contains the (optional) keys:
    * **device_name** (str): The device name (for example, /dev/sdh or xvdh).
    * **ebs** (dict): Parameters used to automatically set up EBS volumes when the instance is launched.
        * **volume_type** (str): The volume type. Valid Values: standard, io1, io2, gp2, sc1, st1, gp3.
        * **volume_size** (int): The size of the volume, in GiBs.
        * **kms_key_id** (str): Identifier (key ID, key alias, ID ARN, or alias ARN) for a customer managed CMK under which the EBS volume is encrypted.
        * **iops** (str): The number of I/O operations per second (IOPS). For gp3, io1, and io2 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
        * **delete_on_termination_** (bool): Indicates whether the EBS volume is deleted on instance termination.
* **kvm_host** (dict): Information about the host running the KVM hypervisr that are dynamically added to the inventory.
        * **volume_size** This variable enabled you to assign the newly added host to one or more groups in the inventory.
* **kvm_host** (dict): Information about the host running the KVM hypervisr that are dynamically added to the inventory.
    * **name**: This is a user-defined name for the host you are adding to the inventory.
    * **ansible_host**: This variable specifies the hostname or IP address of the host you are adding to the inventory.
    * **ansible_user**: This variable specifies the SSH username that Ansible should use when connecting to the host.
    * **ansible_ssh_private_key_file** This variable specifies the path to the SSH private key file that Ansible should use for authentication when connecting to the host.
    * **groups** This variable enabled you to assign the newly added host to one or more groups in the inventory.

## Example Usage

Create a `credentials.yaml` file with the folling contents:

```yaml
aws_access_key: "xxxxxxxxxxxxxxxxxxxx"
aws_secret_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aws_region: "us-east-1"
```

To migrate an existing on prem VM running on KVM hypervisor to AWS, run:

```bash
ansible-playbook move_vm_from_on_prem_to_aws.yml -e "@credentials.yaml"
```
