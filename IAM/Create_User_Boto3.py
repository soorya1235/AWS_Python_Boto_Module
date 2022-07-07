import boto3

def createuser(username):
    iam = boto3.client('iam')
    res = iam.create_user(UserName=username)
    print(res)


createuser('sample')

