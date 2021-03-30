import boto3
import random
import os

sqs = boto3.client('sqs')

## Substitute the AWS account number
queueUrl = 'https://sqs.us-east-1.amazonaws.com/521878158907/demo-decoupling-saa'
    
for i in range(1100): ##update with the nummber of messages you want to send to the queue 
    message = random.choice(range(100000001, 999999999))
    response = sqs.send_message(
        QueueUrl=queueUrl,
        MessageBody=str(message)
    )