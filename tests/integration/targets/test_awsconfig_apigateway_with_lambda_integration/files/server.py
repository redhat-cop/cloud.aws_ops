#!/usr/bin/env python

import json


def lambda_handler(event, context):
    resource_prefix = event.get("queryStringParameters", {}).get("resource_prefix")
    path = event.get("pathParameters", {}).get("proxy")

    message = ""
    if path == "ansible-test":
        message = "Running ansible-test with Resource prefix {0}".format(
            resource_prefix
        )

    return {
        "statusCode": 200,
        "body": json.dumps(message, indent=2),
        "headers": {"Content-Type": "application/json"},
    }
