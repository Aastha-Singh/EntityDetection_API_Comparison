from google.cloud import vision
import os
from google.cloud.vision import types
import io
import pandas as pd
import glob

client = vision.ImageAnnotatorClient()

data = []
image_data = glob.glob('----path to folder -------/*')
for i in image_data:
	frame_name = i.split('/')[-1]
	image_file = io.open(i, 'rb')
	content = image_file.read()
	image = types.Image(content=content)
	response = client.label_detection(image=image)
	labels = response.label_annotations
	for label in labels:
		#print(frame_name, label.description)
		data.append([frame_name,label.description])
pd.DataFrame(data).to_csv('-------path to csv -----/cloud_vision_data_try.csv',index =False)
		
