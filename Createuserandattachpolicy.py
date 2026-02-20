import boto3

iam = boto3.client("iam")

username = "new-dev-user"

iam.create_user(UserName=username)

iam.attach_user_policy(
    UserName=username,
    PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
)

print("IAM user created and policy attached")
