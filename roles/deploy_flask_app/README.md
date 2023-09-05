deploy_flask_app
==================

A role to deploy a simple flask application with RDS db cluster as backend.

Requirements
------------

AWS User Account with the following permission:

* ec2:DescribeInstanceAttribute
* ec2:DescribeInstanceStatus
* ec2:DescribeInstances
* ec2:RunInstances
* ec2:CreateKeyPair
* elb:CreateLoadBalancer
* rds:DescribeDBInstances
* rds:DescribeDBSubnetGroups
* rds:ListTagsForResource

Role Variables
--------------

## variables to create new hosts and groups in inventory of in memory playbook.

* **region** (str): Region where the app is to be deployed.
* **bastion_host_username** (str): Username for the bastion host SSH user.
* **private_subnet_id** (str): Private subnet id of the bastion host
* **vpc_id** (str): vpc id for the host.
* **rds_info** (dict): A dict of information for the backend RDS. This dict has the output of amazon.aws.rds_instance_info mode.
* **rds_master_username** (str): Username for the RDS instance.
* **rds_master_password** (str): password for the RDS instance.
* **vm_info** (dict): A dict of information for the vm to use. This dict has the output of amazon.aws.ec2_instance_info module.

## variables needed for the deployment

# Bastion host
* **bastion_host_name** (str): Name for the EC2 instance.
* **bastion_host_required_packages** (list): Packages to be installed on the bastion host.
* **number_of_workers** (int): Number of instances to create.
* **workers_instance_type** (str): RC2 instance type for workers.

# App
* **app_git_repository** (str): Git repository to be cloned for the webapp.
* **app_listening_port** (int): Load balancer port.
* **app_force_init** (bool): A boolean value True to force init the app and False to not force init.
* **local_registry_user** (str): Registry user name.
* **local_registry_pwd** (str): Registry password.
* **app_config** (dict): A dict of config parameterys for the app.
    **env** (str): Flask env.
    **admin_user** (str): App config's admin username.
    **admin_password** (str): App config's admin password.
    **app_dir** (str): App directory.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

This role takes care of adding the bastion host to the inventory and deploying the app. You can use the deploy_flask_app role after setting up the necessary resources.The resources required for using the app are

* RDS cluster and instances.
* A Bastion host.
* SSH key pair to connect to the host.

The setup of these resources needed for the app deployment can be done using a playbook similar to this [sample playbook]((https://github.com/ansible-collections/cloud.aws_ops/roles/deploy_flask_app/files/create.yaml).

**Deploy a simple flask app**

- name: Deploy resource from Bastion
  hosts: bastion
  gather_facts: false

  module_defaults:
    group/aws:
      aws_access_key: "{{ aws_access_key }}"
      aws_secret_key: "{{ aws_secret_key }}"
      security_token: "{{ security_token | default(omit) }}"
      region: "{{ aws_region }}"

  vars_files:
    - [vars.yaml](https://github.com/ansible-collections/cloud.aws_ops/roles/deploy_flask_app/files/vars/main.yaml)

  tasks:
    - name: Deploy app
      ansible.builtin.import_tasks: deploy_app.yaml

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
