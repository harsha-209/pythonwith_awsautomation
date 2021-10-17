import boto3

iam_console=boto3.client('iam')

## below two steps helps what are avaiable features for iam section , it desplayes to us
#response = dir(iam_console)
#print(response)


##################### create a iam user ###################################################
#response = iam_console.create_user(UserName='satti')

#print(response)

######################### list all users ################################################
#response=iam_console.list_users()
#print(response)

######################## list only usernames#############################################

#response=iam_console.list_users()['Users']


###print(response['UserName'])  it error we can use slic operator


########################## list user using for###########################
#response=iam_console.list_users()['Users']

#for iamusers in response:
#    print(iamusers['UserName'])

##print(dir(iam_console))


#######################33 deleting a user from iam console############################

###response=iam_console.delete_user(UserName='satti')

###print(response)


###################### list  polices 
