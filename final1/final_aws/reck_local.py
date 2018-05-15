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
import pandas as pd
import glob
image_data = glob.glob('----path to folder-----/*.jpg')
client=boto3.client('rekognition','us-east-1')

print(image_data)
final_data = []

for i in image_data:
        imageFile=i
        with open(imageFile, 'rb') as image:
                response = client.detect_labels(Image={'Bytes': image.read()})
        
                #print('Detected labels in ' + imageFile)    
                for label in response['Labels']:
                        #print (label['Name'] + ' : ' + str(label['Confidence']))
                        final_data.append([i,label['Name'] + ' _ ' + str(label['Confidence'])])
pd.DataFrame(final_data).to_csv('try.csv', index = False)


