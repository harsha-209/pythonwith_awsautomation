
import boto3


ec2_cons = boto3.client('ec2')

response = ec2_cons.describe_security_groups()['SecurityGroups']
for each in response:
    #print(each['GroupId'])
    secu_id = each['GroupId']
    print(secu_id)
######################################### deleting all security groups in mumbai region#################
    responsed = ec2_cons.delete_security_group(
    GroupId=secu_id)
    print(responsed)

