import io
import boto3
myclient=boto3.client('ec2', region_name="ap-northeast-3")

key_pair=myclient.create_key_pair(KeyName="Aditya_key")
data=key_pair["KeyMaterial"]

print(data)

with io.open("Aditya_key.pem","w",encoding="utf-8") as f1:
    f1.write(str(data))
    f1.close()
    