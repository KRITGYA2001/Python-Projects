#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Detector import *


# In[2]:


#modelURL="http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz"

#modelURL="http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz"


# In[3]:


modelURL="http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_640x640_coco17_tpu-8.tar.gz"


# In[6]:


classFile="coco.names"
#imagePath="2.jpg"
videoPath=0 #"sample2.mp4"              #0 for webcam
threshold=0.5
detector=Detector()
detector.readClasses(classFile)
detector.downloadModel(modelURL)
detector.loadModel()
#detector.predictImage(imagePath,threshold)
detector.predictVideo(videoPath,threshold)


# In[ ]:




