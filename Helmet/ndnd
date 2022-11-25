from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import os
import cv2

images_frames = 'image_frames'

def files():
    try:
        os.remove(images_frames)
    except OSError:
        pass
    
    if not os.path.exists(image_frames):
        os.makedirs(images_frames)
        
    src_vid = cv2.VideoCapture('#le fichier video a voir')
    return(src_vid)

def process(src_vid):
    index = 0
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        if not ret:
            break
        
        name = './image_frames/frame' + str(index) + '.png'
        
        if index % 100 == 0:
            print('Extracting frames...' + name)
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitkey(10) & 0xFF == ord('q'):
            break
    
    src_vid.release()
    cv2.destroyAllWindows()
    
def get_text():
    for i in os.listdir(images_frames):
        print(str(i))
        myexample = Image.open(image_frames + "/" + i)
        text = pytesseract.image_to_string(myexample, lang='eng')
        print(text)
        

if __name__== '__main__':
    vid = files()
    process(vid)
    get_text()