import boto3

def lambda_handler(event, context):
    ec2_cons = boto3.client('ec2')
    filter_custome = {'Name': 'tag:Name','Values': ['workernode',]}
    response = ec2_cons.describe_instances(Filters=[filter_custome])
    for each in response['Reservations']:
        for each_value in each['Instances']:
            print(each_value['InstanceId'])