import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["harshad"]}

response = ec2_con.create_volume(
    AvailabilityZone='ap-south-1a',
    Encrypted=False,
    Size=8,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'harshad'
                },
            ]
        },
    ]
)


print(response)
