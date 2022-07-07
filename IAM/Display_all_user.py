import boto3

client = boto3.client('iam')
paginator = client.get_paginator('list_users')
print(paginator)

for response in paginator.paginate():
    for users in response['Users']:
        print("User Name is {} and ARN is {}".format(users['UserName'],users['Arn']))
