import boto3
import json


iam_cons=boto3.client('iam')

#print(dir(iam_cons))

policy_json = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CognitoPostConfirmationAddToGroup",
            "Effect": "Allow",
            "Action": "cognito-idp:AdminAddUserToGroup",
            "Resource": "arn:aws:cognito-idp:ap-northeast-1:585584209241:userpool/ap-northeast-1_p48aaPoti"
        }
    ]   
}

create_policyresponse = iam_cons.create_policy(
    PolicyName='harshad12',
    Path='/',
    PolicyDocument=json.dumps(policy_json)
)

print(create_policyresponse)


################################ creating a role ##########################################

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

createrole_response = iam_cons.create_role(
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Path='/',
    RoleName='Test-Role1',
)

print(createrole_response)


####################### attaching a role to policy ################################
attach_rolepolicyresponse = iam_cons.attach_role_policy(
    RoleName='Test-Role1',
    PolicyArn='string'
)

print(attach_rolepolicyresponse)
