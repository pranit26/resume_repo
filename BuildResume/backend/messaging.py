# backend/messaging.py
from io import BytesIO
import boto3
from botocore.exceptions import NoCredentialsError
from django.core.files.base import ContentFile

 
sqs_send = boto3.client('sqs',aws_access_key_id="my_access_key",aws_secret_access_key="aws_secret_access_key",region_name='ap-south-1')

s3 = boto3.client('s3',aws_access_key_id="aws_secret_access_key",aws_secret_access_key="aws_secret_access_key",region_name='ap-south-1')

def notify_backend(id,resume_content):
    try:
        queue_url = "https://sqs.ap-south-1.amazonaws.com/678735747955/resume"
        message_body = f'New candidate created with ID: {id}'
        res=sqs_send.send_message(QueueUrl=queue_url,MessageBody=message_body,MessageAttributes=resume_content)
        return res
    except Exception as e:
        print(e)
        return False
    


def upload_to_s3(file_content, file_name, bucket_name='resumebucket14'):
    try:        
        with BytesIO(file_content) as binary_content:
            s3.upload_fileobj(binary_content, bucket_name, file_name)    

        print("File uploaded successfully")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False    
   