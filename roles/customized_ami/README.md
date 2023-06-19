# customized_ami

A role to create custom AMI on AWS. User can create, update or delete AMI.

## Requirements

AWS credentials with valid permission.

## Role Variables

- **custom_ami_operation** - Operation to perform. Valid values are 'create', 'delete'.
- **custom_ami_name** - Name of the AMI to create. **Required**
- **custom_ami_packages** - List of packages to install. **Required**
- **custom_ami_recreate_if_exists** - Whether to recreate the AMI if it already exists, default value is False.
- **source_ami_filters** - A dict of filters to apply to find the source AMI id. See [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) for possible filters.
- **source_ami_image_id** - Image id of the AMI to be used as source. When not specified, we will use **source_ami_filters** to determine source AMI image id.
- **source_ami_user_name** - User name to connect to EC2 instance used to create custom AMI. Default value is **ec2-user**.

## Dependencies

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example Playbook

    - hosts: servers
      roles:
         - role: cloud.aws_ops.customized_ami
           custom_ami_name: my_customized_ami_name
           custom_ami_packages:
            - package1
            - package2
            - package3

## License

GNU General Public License v3.0 or later
