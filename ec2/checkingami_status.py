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
'''
################# checking ami status ############################
image = ec2_cons.describe_images(ImageIds=[instance_amid])
#image = ec2_cons.describe_images(ImageIds=['ami-0b2b1a277c3691d29'])
for each in image['Images']:
    print(each['State'])
'''

while True:
    status_image = ec2_cons.describe_images(ImageIds=[instance_amid])['Images']
    #status_image[0]['State']
    if status_image[0]['State'] == "available":
        break
    time.sleep(10)
    print("checking")
print("ami is now available")
    








'''
    if(each['State'] == 'pending'):
        print("Waiting for image to be available.")
        while(each['State'] != 'available'):
            image = ec2_cons.describe_images(ImageIds=[instance_amid])
        print("Image Available to use")

        '''