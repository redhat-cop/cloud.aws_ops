.. _redhat_cop.cloud.aws_ops.docsite.eda_guide:


How to integrate Event-driven Ansible with this Ansible Validated Content Collection
====================================================================================

Event-driven Ansible refers to a method of running Ansible that allows it to respond automatically to events occurring within a system. This approach allows Ansible to react to changes in real-time and automate responses to events such as configuration changes, application failures, or security breaches. For example, if a server goes down, Ansible can be configured to automatically start up a new server to replace it.
To use event-driven Ansible, it is needed to configure Ansible to listen for specific events and set appropriate triggers to execute playbooks in response.
Overall, event-driven Ansible can be an extremely powerful tool for automating and managing complex systems, but it does require a good deal of planning and configuration to set up and maintain. More information on this initiative can be found [here](https://www.ansible.com/use-cases/event-driven-automation).

To enable Event-driven Ansible in the cloud.aws_ops Collection, we have created two folders:
1. `rulesbooks` hosts the rulebook that tells the system what events to flag and how to respond to them.
2. `playbooks/eda` hosts the playbooks that implement the logic to mitigate the drift. Each of the playbooks inside `playbooks/eda`` handle a specific drift.

Let's take a look at the rulebook:

```yaml
   - name: Rules for cloud.aws_ops to ensure the CloudTrail exists and is encrypted
     hosts: all

     sources:
      - ansible.eda.aws_cloudtrail:
          region: vars.region_name
          delay_seconds: 5
     rules:
      - name: Enable Trail encryption
        condition: event.CloudTrailEvent.eventName=="UpdateTrail" and event.CloudTrailEvent.requestParameters.kmsKeyId=="" and event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name
         action:
           run_playbook:
             name: playbooks/eda/aws_restore_cloudtrail_encryption.yml

      - name: Re-create the CloudTrail
        condition: event.CloudTrailEvent.eventName=="DeleteTrail" and event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name
        action:
          run_playbook:
             name: playbooks/eda/aws_restore_cloudtrail.yml

      - name: Cancels the deletion of the KMS key and re-enables it
        condition: event.CloudTrailEvent.eventName=="ScheduleKeyDeletion" or event.CloudTrailEvent.eventName=="DisableKey"
        action:
          run_playbook:
             name: playbooks/eda/aws_restore_kms_key.yml
```

A rulebook is comprised of three main components:
1. `sources` define which event source we will use.
2. `rules` define conditionals we will try to match from the event source.
3. `actions` trigger what you need to happen should a condition be met.

In our case, we  used the [ansible.eda.aws_cloudtrail](https://github.com/ansible/event-driven-ansible/blob/main/plugins/event_source/aws_cloudtrail.py) event source plugin for getting events from an AWS CloudTrail.
This plugin polls events from an AWS CloudTrail every 5 seconds. Next, this rulebook implements a ruleset with three rules as follows:

Rule #1: Enable trail encryption
--------------------------------
This rule handles the case when trail encryption is disabled. It is triggered when an "UpdateTrail" operation is performed on the trail and the parameters contained in the "UpdateTrail" request match these conditions: `event.CloudTrailEvent.requestParameters.kmsKeyId=="" and event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name`. The action that is taken to mitigate this drift will run the `playbooks/eda/aws_restore_cloudtrail_encryption.yml` playbook. This playbook runs the Ansible Validated role `cloud.aws_ops.enable_cloudtrail_encryption_with_kms` that re-enable the trail's encryption, restoring the system to its status quo.

Rule #2: Re-create the trail
----------------------------
This rule handles the case when the trail is deleted. Basically, when these conditions `event.CloudTrailEvent.eventName=="DeleteTrail" and event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name` are met, the action to be takes implies running the `playbooks/eda/aws_restore_cloudtrail.yml` playbook. This playbook runs the Ansible Validated Content `cloud.aws_ops.awsconfig_multiregion_cloudtrail` role first which re-creates the trail and then the `cloud.aws_ops.enable_cloudtrail_encryption_with_kms` role to enable the encryption on the newly created trail.

Rule #3: Cancels the deletion of the KMS key and re-enables it
--------------------------------------------------------------
This rule handles the case when the KMS key is deleted or disabled. This results in the condition `event.CloudTrailEvent.eventName=="ScheduleKeyDeletion" or event.CloudTrailEvent.eventName=="DisableKey"` that should be met to trigger this rule. When someone attempts to delete a KMS key intentionally or accidentally, a "ScheduleKeyDeletion" event is displayed in AWS CloudTrail. The KMS key is not deleted immediately; because deleting a KMS key is destructive and potentially dangerous, AWS KMS requires setting a 7-30 day waiting period. This situation is handled promptly by running `playbooks/eda/aws_restore_kms_key.yml` playbook which cancels the deletion of the KMS key. Similarly, when the KMS is disabled, the playbook reactivates it to restore the original state of the system.

The playbook sets the KMS key ARN and uses it to determine whether to both cancel the KMS key deletion and to re-enable it.

Follow the instructions defined in the README of [ansible/event-driven-ansible](https://github.com/ansible/event-driven-ansible#install) to install the collection and its dependencies.

The rulebook is executed with the following command:

```shell
    ansible-rulebook --inventory inventory.yml --rulebook rulebooks/aws_manage_cloudtrail_encryption.yml --vars vars.yml
```

The inventory file used is like:

```yaml
  all:
    hosts:
    localhost:
        ansible_python_interpreter: /path/to/python
        ansible_connection: local
```

While, `vars.yml` file looks like:

```yaml
    _resource_prefix: ansible-cloudtrail-demo-eda
    cloudtrail_name: "{{ _resource_prefix }}-trail"
    s3_bucket_name: "{{ _resource_prefix }}-bucket"
    kms_key_alias: "{{ _resource_prefix }}-key"
    key_prefix: "{{ _resource_prefix }}"
    region_name: us-east-1
```
