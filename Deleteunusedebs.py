import boto3

ec2 = boto3.client("ec2")

volumes = ec2.describe_volumes()

for volume in volumes["Volumes"]:
    if volume["State"] == "available":
        volume_id = volume["VolumeId"]
        print(f"Deleting {volume_id}")
        ec2.delete_volume(VolumeId=volume_id)
