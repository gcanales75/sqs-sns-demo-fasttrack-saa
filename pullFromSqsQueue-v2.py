import boto3
import random
import os
import socket
import time
from sys import exit

sqs = boto3.client('sqs')
dynamodb = boto3.resource('dynamodb')
sts = boto3.client('sts')

tableName = 'fasttracksaa'

queueUrl = 'https://sqs.us-east-1.amazonaws.com/521878158907/demo-decoupling-saa'
#queueUrl = 'https://sqs.us-east-1.amazonaws.com/$ACCOUNT_NUMBER/demo-decoupling-saa'


while True:
    response = sqs.receive_message(
    QueueUrl=queueUrl,
    MaxNumberOfMessages=1
    )
    message_in_response =  "Messages" in response
    print(message_in_response)
    if message_in_response == False:
        break
    else:
        message = response['Messages'][0]['Body']
        receiptHandle = response['Messages'][0]['ReceiptHandle']

        table = dynamodb.Table(tableName)

        putItem = table.put_item(
            Item={
                'queueMessage': message,
                'host': socket.gethostname()
            }
        )
        deleteMsg = sqs.delete_message(
            QueueUrl=queueUrl,
            ReceiptHandle=receiptHandle
        )
        time.sleep(1)