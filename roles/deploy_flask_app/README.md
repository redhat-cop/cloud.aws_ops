manage_transit_gateway
==================

A role to deploy a simple flask application with RDS db cluster as backend.

Requirements
------------

AWS User Account with the following permission:

* ec2:CreateKeyPair
* ec2:DescribeInstances
* ec2:RunInstances
* elb:CreateLoadBalancer

Role Variables
--------------

## variables to create new hosts and groups in inventory of in memory playbook.

* **region**: Region where the app is to be deployed.
* **private_subnet_id**: Private subnet id of the bastion host
* **vpc_id**: vpc id for the host.
* **rds_info**: A dict of information for the backend RDS
    **aws_postgresql_dbname**: postgresql DB name. default: 'mysampledb123'.
    **aws_postgresql_master_user**: postgresql DB user name. default: 'ansible'.
    **aws_postgresql_master_password**: postgresql DB password. default: 'L#5cH2mgy_'.

## variables need for the deployment
* **bastion_host_required_packages**: packages to be installed on the bastion host.
* **bastion_host_required_packages**: name of the bastion host.
* **number_of_workers**: number of instances to create.
* **workers_instance_type**: type of instance.
* **app_git_repository**: git repository to be cloned for the webapp.
* **app_listening_port**: load balancer port.
* **app_force_init**: A boolean value True to force init the app and False to not force init.
* **rds_listening_port**: Listening port for the RDS.
* **local_registry_user**: Registry user name.
* **local_registry_pwd**: Registry password.
* **app_config**: A dict of config parameterys for the app.
    **env**: Flask env.
    **admin_user**: App config's admin username.
    **admin_password**: App config's admin password.
    **app_dir**: App directory.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

The setup of resources needed for the app deployment can be done using a playbook similar to this [sample playbbok]((https://github.com/ansible-collections/cloud.aws_ops/roles/deploy_flask_app/files/create.yaml).

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
