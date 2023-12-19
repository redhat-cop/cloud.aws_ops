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

* **deploy_flask_app_region** (str): Region where the app is to be deployed.
* **deploy_flask_app_private_subnet_id** (str): Private subnet id of the bastion host
* **deploy_flask_app_vpc_id** (str): vpc id for the host.
* **deploy_flask_app_rds_info** (dict): A dict of information for the backend RDS. This dict has the output of amazon.aws.rds_instance_info mode.
* **deploy_flask_app_rds_master_username** (str): Username for the RDS instance.
* **deploy_flask_app_rds_master_password** (str): password for the RDS instance.
* **deploy_flask_app_vm_info** (dict): A dict of information for the vm to use. This dict has the output of amazon.aws.ec2_instance_info module.

## variables needed for the deployment

# Bastion host
* **deploy_flask_app_bastion_host_name** (str): Name for the EC2 instance.
* **deploy_flask_app_bastion_host_username** (str): Username for the bastion host SSH user.
* **deploy_flask_app_bastion_host_required_packages** (list): Packages to be installed on the bastion host.
* **deploy_flask_app_sshkey_pair_name** (str): Name for the EC2 key pair.
* **deploy_flask_app_bastion_ssh_private_key** (path): The path to the ssh private key file to use to connect to the bastion host.
* **deploy_flask_app_number_of_workers** (int): Number of instances to create.
* **deploy_flask_app_workers_instance_type** (str): RC2 instance type for workers.
* **deploy_flask_app_workers_user_name** (str): Username for the workers.

# App
* **deploy_flask_app_git_repository** (str): Git repository to be cloned for the webapp.
* **deploy_flask_app_listening_port** (int): Load balancer port.
* **deploy_flask_app_force_init** (bool): A boolean value True to force init the app and False to not force init.
* **deploy_flask_app_local_registry_port** (int): Port for the local Podman registry.
* **deploy_flask_app_local_registry_user** (str): Registry user name.
* **deploy_flask_app_local_registry_pwd** (str): Registry password.
* **deploy_flask_app_config** (dict): A dict of config parameterys for the app.
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

The setup of these resources needed for the app deployment can be done using a playbook similar to this [playbook](https://github.com/ansible-collections/cloud.aws_ops/playbooks/webapp/tasks/create.yaml).

**Deploy a simple flask app**

- name: Import Deploy Flask App Role
  hosts: localhost
  gather_facts: false

  vars_files:
    - [vars.yaml](https://github.com/ansible-collections/cloud.aws_ops/playbooks/webapp/vars/main.yaml)

  tasks:
    - name: Deploy app
      ansible.builtin.import_role: deploy_flask_app.yaml

- name: Use Deploy Flask App Role
  hosts: localhost
  roles:
    - role: cloud.aws_ops.deploy_flask_app
      vars:
        - [vars.yaml](https://github.com/ansible-collections/cloud.aws_ops/playbooks/webapp/vars/main.yaml)


License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
