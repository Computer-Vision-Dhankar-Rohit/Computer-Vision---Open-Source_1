### Positive URL -- RIFLES Pics --- http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02907391


# 29 SEP 17 

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    #neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02960352' ## Cars No Rifles 
    #neg_images_link = ' ' ## SPORTSMEN -- Footballers -- People Without RIFLES 
    
    ### We get down Images of Peeps w/o RiFLES and keep that as the NEGATIVE Data Set
    
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('blah'):
        os.makedirs('/media/dhankar/Dhankar_1/a10_17/Own_Haar/neg/No_Rifles')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  

## Run the Function Defined Above ...without any ARGUMENTS or PARAMETERS            
store_raw_images()
