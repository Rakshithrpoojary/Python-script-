import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters=[
        {"Name": "tag:Environment", "Values": ["Dev"]}
    ]
)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        print(f"Starting {instance_id}")
        ec2.start_instances(InstanceIds=[instance_id])
