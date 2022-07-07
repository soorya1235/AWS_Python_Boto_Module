import boto3
import json

client = boto3.client('iam')
user_policy = {
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect" : "Allow",
            "Action" : "*",
            "Resource" : "*"
        }
    ]
}

response = client.create_policy(
    PolicyName = "mypolicy",
    PolicyDocument = json.dumps(user_policy))

print(response)


