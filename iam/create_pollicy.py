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