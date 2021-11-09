import boto3
import json


iam_cons=boto3.client('iam')



list_response = iam_cons.list_policies(
    Scope='Local')['Policies']

#print(list_response)

for policesiam in list_response:
 #  print(policesiam['PolicyName'])
    print(policesiam['Arn'])
    
  
