import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client(
    service_name='s3',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY')
)

response = s3_client.upload_file('superheroes.csv', os.getenv('AWS_S3_BUCKET_NAME'), 'superheroes.csv')
print(f'Upload file response: {response}')