from urllib import response
import boto3

s3=boto3.client("s3")
# bucket=s3.create_bucket(Bucket="adi-bucket-create")
response=s3.create_bucket(Bucket="sayani-bucket-create-hoye-jak",
    CreateBucketConfiguration={
        'LocationConstraint':'ap-northeast-3'
    },
)
print(response)


