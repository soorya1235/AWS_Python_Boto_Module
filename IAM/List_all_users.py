import boto3

client = boto3.client('iam')

def list_policies():
    paginator = client.get_paginator('list_policies')
    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name =  policy['PolicyName']
            Arn = policy['Arn']
            print("Policy Name is {} and Arn is {}".format(policy_name,Arn))


list_policies()