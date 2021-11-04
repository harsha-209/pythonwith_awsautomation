import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'name','Values': ["my_customeami"]}

response = ec2_con.describe_images(
    Filters=[
        {
            'Name': 'name',
            'Values': [
                'my_customeami',
            ]
        },
    ],
    Owners=[
        'self',
    ]
)


delete_amid = response['Images'][0]['ImageId']

##################################3 deleteing or deregistering  a specific ami ###############################
deleteami = ec2_con.deregister_image(
    ImageId=delete_amid
)

print(deleteami)
