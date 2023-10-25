clone_on_prem_vm
================

A role to clone an existing on prem VM using the KVM hypervisor. The role sets the **clone_on_prem_vm_raw_image_path** variable containing the path where the image was saved on localhost. This role requires privilege escalation because the .qcow2 file created by ``virt-clone`` is owned by root and ``qemu-img convert`` requires access to convert it to .raw.

Requirements
------------

**qemu** and **qemu-img** packages installed.

Role Variables
--------------

* **clone_on_prem_vm_source_vm_name**: (Required) The name of the on-prem VM you want to clone.
* **clone_on_prem_vm_image_name**: (Optional) The name you want to call the cloned image. If not set, the **clone_on_prem_vm_source_vm_name** will be used with a _-clone_ suffix.
* **clone_on_prem_vm_overwrite**: (Optional) Whether to overwrite or not an already existing on prem VM clone. Default: true.
* **clone_on_prem_vm_local_image_path**: (Optional) The path where you would like to save the image. If the path does not exists on localhost, the role will create it. If this parameter is not set, the role will save the image in a _~/tmp_ folder.
* **clone_on_prem_vm_uri**: (Optional) Libvirt connection uri. Default: "qemu:///system".

Dependencies
------------

N/A

Example Playbook
----------------

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
- hosts: kvm
  gather_facts: true

  tasks:
    - name: Import 'cloud.aws_ops.clone_on_prem_vm' role
      ansible.builtin.import_role:
        name: cloud.aws_ops.clone_on_prem_vm
      vars:
        clone_on_prem_vm_source_vm_name: "{{ clone_on_prem_vm_source_vm_name }}"
        clone_on_prem_vm_image_name: "{{ clone_on_prem_vm_image_name }}"
        clone_on_prem_vm_local_image_path: "{{ clone_on_prem_vm_local_image_path }}"
        clone_on_prem_vm_uri: "{{ clone_on_prem_vm_uri }}"
```

Run the playbook:

```shell
ansible-playbook playbook.yml -i inventory.yml -e "@vars.yml"
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
