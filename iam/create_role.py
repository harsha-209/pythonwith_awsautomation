import boto3

import json

iam_cons=boto3.client('iam')







assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "greengrass.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}

response = iam_cons.create_role(
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Path='/',
    RoleName='Test-Role',
)

print(response)

