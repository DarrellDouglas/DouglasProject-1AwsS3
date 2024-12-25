import boto3 # type: ignore

# Create the S3 client
client = boto3.client('s3',
    aws_access_key_id="",
    aws_secret_access_key=""
)

# Fetch the list of buckets
response = client.list_buckets()

# Print only the bucket names
print("Your S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
