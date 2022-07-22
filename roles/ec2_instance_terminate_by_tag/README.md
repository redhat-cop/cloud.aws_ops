ec2_instance_terminate_by_id
==================

A role to terminate the ec2_instances having tag 'ToTerminate':  True.

In the role vars, if 'terminate_tagged_instances' is set to True, all the instances with tag
'ToTerminate': True will be terminated.
