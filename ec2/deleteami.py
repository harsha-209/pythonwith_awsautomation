import boto3

ec2_cons = boto3.client('ec2')


image = ec2_cons.deregister_image(
    ImageId='ami-01f055cbfa60ba9bf',
)


print(image)