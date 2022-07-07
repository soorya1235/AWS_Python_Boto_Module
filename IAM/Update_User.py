import boto3

client = boto3.client('iam')
def update_user(oldusername,newusername):
    response = client.update_user(
    UserName=oldusername,
    NewUserName=newusername)
    print(response)


update_user('soorya','jacckysheraf')