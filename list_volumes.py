import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["harshad"]}

response = ec2_con.describe_volumes(
    Filters=[
        {
            'Name': 'size',
            'Values': [
                '8',
            ]
        },
    ]
)


#print(response['Volumes'][0]['Attachments'][0]['VolumeId'])

for each_volume in response['Volumes']:
    for each_item in each_volume['Attachments']:
        print(each_item['VolumeId'])
