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

#print(response['Volumes'][0]['VolumeId'])
################################### deleting a volume #######################################
for each_volume in response['Volumes']:
    print(each_volume['VolumeId'])
    delete_volume = ec2_con.delete_volume(VolumeId=each_volume['VolumeId'])
    print(delete_volume)
