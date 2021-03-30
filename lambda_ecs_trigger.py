from __future__ import print_function
import json
import urllib3
import logging
import boto3
from botocore.exceptions import ClientError
import time
import os
from sys import exit

ecs = boto3.client('ecs')

subnet1 = os.environ["subnet1"]
subnet2 = os.environ["subnet2"]
sg = os.environ["secgroup"]

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    response = ecs.run_task(
        cluster='FastTrack-Saa-Sqs-demo',
        count=4,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [ subnet1, subnet2 ],
                'securityGroups': [ sg ],
                'assignPublicIp': 'ENABLED'
            }
        },
        taskDefinition='fasttrack-saa-td'
    )