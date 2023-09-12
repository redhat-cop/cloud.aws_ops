Role Name
=========

A role to migrate an existing on prem VM to AWS.

Requirements
------------

AWS User Account with the following permissions:


Role Variables
--------------

* **move_vm_from_on_prem_to_aws_on_prem_vm_name**: (Required) The  name of the on-prem VM you want to clone.
* **move_vm_from_on_prem_to_aws_bucket_name**: (Required) The name of the S3 bucket name where you want to upload the .raw image.
* **move_vm_from_on_prem_to_aws_on_prem_instance_name**: (Required) The name of the EC2 instance you want to create using the imported AMI.
* **move_vm_from_on_prem_to_aws_instance_type**: The EC2 instance type you want to use. Default: "t2.micro".
* **move_vm_from_on_prem_to_aws_keypair_name**: The name of the SSH access key to assign to the EC2 instance. It must exist in the region the instance is created. If not set, your default AWS account keypair will be used.
* **move_vm_from_on_prem_to_aws_security_group**: A list of security group IDs or names to assiciate to the EC2 instance.
* **move_vm_from_on_prem_to_aws_vpc_subnet_id**: The subnet ID in which to launch the EC2 instance instance (VPC). If none is provided, M(amazon.aws.ec2_instance) will chose the default zone of the default VPC.
* **move_vm_from_on_prem_to_aws_uri**: (Required) # Libvirt connection uri.Default: "qemu:///system".
* **move_vm_from_on_prem_to_aws_volumes**: A dictionary of a block device mappings, by default this will always use the AMI root device so the **move_vm_from_on_prem_to_aws_volumes** option is primarily for adding more storage. A mapping contains the (optional) keys _device_name_, _ebs.volume_type_, _ebs.volume_size_, _ebs.kms_key_id_, _ebs.iops_, and _ebs.delete_on_termination_.


Dependencies
------------

- role: cloud.aws_ops.aws_setup_credentials

Example Playbook
----------------

    - hosts: localhost

    - ansible.builtin.import_role:
        name: cloud.aws_ops.move_vm_from_on_prem_to_aws
      vars:
        move_vm_from_on_prem_to_aws_on_prem_vm_name: "test-vm"
        move_vm_from_on_prem_to_aws_on_prem_bucket_name: "test-s3-bucket"
        move_vm_from_on_prem_to_aws_on_prem_instance_name: "test-instance-name"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.azure_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
