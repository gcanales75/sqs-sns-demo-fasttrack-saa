import boto3
import random
import os
import socket
import time
from sys import exit

sqs = boto3.client('sqs')
#dynamodb = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

tableName = 'demo-decoupling-saa'
queueUrl = 'https://sqs.us-east-1.amazonaws.com/521878158907/demo-decoupling-saa'

for i in range(2):
    response = sqs.receive_message(
        QueueUrl=queueUrl,
        MaxNumberOfMessages=1
    )
    #print(response)
    message_in_response =  "Messages" in response
    print(message_in_response)
    if message_in_response == True:

        message = response['Messages'][0]['Body']
        receiptHandle = response['Messages'][0]['ReceiptHandle']
        #print(message)
        #print(receiptHandle)

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
        #time.sleep(1)
    
    else:
        exit
