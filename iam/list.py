import boto3


iam_con = boto3.client('iam')

response = iam_con.list_policies(
    Scope='All',
)

for each in response['Policies']:
    print("this is the policyname {}\n and its arn {}\n".format(each['PolicyName'],each['Arn']))