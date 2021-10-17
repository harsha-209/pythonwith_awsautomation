################### describe instance with specific tags###################################
import boto3
import time

ec2_cons = boto3.client('ec2')

custom_filter = [{'Name':'tag:Name','Values':['master']}]

response = ec2_cons.describe_instances(Filters=custom_filter)

for each in response['Reservations']:
    for each_value in each['Instances']:
        print("instance is launched on {}\n and its instance id is {}\n".format(each_value['LaunchTime'].date(),each_value['InstanceId']))
        instancea_id = each_value['InstanceId']
     #   print(instance_id)
##################### creating ami for above instance #######################################
        image = ec2_cons.create_image(
    
    Description='myown',
    Name='newimage',
    InstanceId=instancea_id,
    NoReboot=False,

)

print(image['ImageId'])
instance_amid = image['ImageId']


###################### listing the ami in specific region ##############################
myown_images = ec2_cons.describe_images(Owners=['self'])
for each in myown_images['Images']:
    print(each['ImageId'])
    print(each['State'])
    print("this ami is created for above instance and ami id is :{}\n and creationtime is {}\n".format(each['ImageId'],each['CreationDate']))

#################### create a instance with above custome image or ami###############################
    