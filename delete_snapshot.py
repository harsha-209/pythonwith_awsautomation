import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["harshad"]}

response = ec2_con.describe_snapshots(
#    Filters=[
#        {
#            'Name': 'string',
#            'Values': [
#                'string',
#            ]
#        },
#    ],
    OwnerIds=[
        'self',
    ]
)

#print(response['Snapshots'])


for  each_snapshot in response['Snapshots']:
     print(each_snapshot['SnapshotId'])
     delete_snapshot = ec2_con.delete_snapshot(SnapshotId=each_snapshot['SnapshotId'])
     print(delete_snapshot)
