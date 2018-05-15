"""
List all S3 object versions
"""
# python dependencies
import numpy as np
import pandas as pd
import os
import tensorflow as tf
from PIL import Image
import json
import logging
import os
from boto.s3.connection import S3Connection
import boto3

#print('--- Connecting to S3')
cx = S3Connection(aws_access_key_id='--- input your aws access key ---',
        aws_secret_access_key='--- input secret access key ---')

#print('--- Selecting the bucket')
bucket = cx.get_bucket('--- name of the S3 bucket where images are ---')
#print(bucket)
bucket1='--- name of the S3 bucket where images are ---'

versions = bucket.list()
#versions = bucket.list(prefix='')
#a = type(versions)
#print(a)

list_files = []
#print('--- List all bucket key versions')
for version in versions:
    c = version.name
    #print(c)
    list_files.append(c)
#print(list_files)
client=boto3.client('rekognition','us-east-1')
#print(client)

final_data = []
for j in list_files:
    fileName = j
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket1,'Name':fileName}})
    #print(response)
    #print('Detected labels for ' + fileName)    
    for label in response['Labels']:
        #print (label['Name'] + ' : ' + str(label['Confidence']))
        final_data.append([j,label['Name'] + ' : ' + str(label['Confidence'])])
pd.DataFrame(final_data).to_csv('--- output folder to save file ---.csv', index = False)
