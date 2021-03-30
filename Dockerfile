FROM python:3

ADD pullFromSqsQueue.py /
RUN pip install boto3

CMD [ "python", "./pullFromSqsQueue.py" ]