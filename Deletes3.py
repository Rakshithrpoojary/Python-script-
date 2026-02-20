import boto3

s3 = boto3.resource("s3")
bucket_name = "my-unique-bucket-12345"

bucket = s3.Bucket(bucket_name)
bucket.delete()

print("Bucket deleted")
