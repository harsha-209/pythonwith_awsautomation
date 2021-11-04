import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["harshad"]}

response = ec2_con.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'harshad',
            ]
        },
    ]
)

print(response['Volumes'][0]['VolumeId'])

############################ creating a  snapshot for respective volume############################

create_snapshot = ec2_con.create_snapshot(
    Description='prod snapshot',
    VolumeId=response['Volumes'][0]['VolumeId'],
    TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'harshad'
                },
            ]
        },
    ]
)

print(create_snapshot)
