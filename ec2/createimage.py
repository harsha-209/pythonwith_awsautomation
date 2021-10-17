import boto3
import time
import datetime

ec2_cons = boto3.client('ec2')


image = ec2_cons.create_image(
    
    Description='myown',
    Name='newimage',
    InstanceId='i-034ea2894db820a43',
    NoReboot=False, 
#    TagSpecifications=[
#        {
#            'ResourceType': 'image',
#            'Tags': [
#                {
#                    'Key': 'Name',
#                    'Value': 'Harshad'
#                },
#            ]
#        },
#    ]

)

print(image['ImageId'])


listimages = ec2_cons.describe_images(Owners=['self'])

for each in listimages['Images']:
    print(each['ImageId'])
    a = each['State']
    

    #for each_value in each['BlockDeviceMappings']:
    #    print(each_value)
        
    #print("this ami is creted just now its id is: {}\n and launchtime is {}\n for this ami parallel snapshot also created is id {}\n".format(each['ImageId'],each['CreationDate'],each['SnapshotId']))