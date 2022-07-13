from urllib import response
import boto3

s3=boto3.resource("s3")
bucket=s3.Bucket("adi-bucket-create")
response=bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'ap-northeast-3'
    },
)
print(response)


