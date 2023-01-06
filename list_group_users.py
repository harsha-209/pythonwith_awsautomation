response = iam.list_groups()
for group in response['Groups']:    
    group_details = iam.get_group(GroupName=group['GroupName'])
    print(group['GroupName'])
    for user in group_details['Users']:
        print(" - ", user['UserName'])
