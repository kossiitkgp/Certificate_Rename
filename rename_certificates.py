
# coding: utf-8

# In[1]:


import os
from PIL import Image
import pytesseract
import argparse


# In[5]:


# loop across all the files in the directory
for file_no,file in enumerate(os.listdir()):
    
    if file.startswith("KWoC"):
        # Get the text from the image
        OCR = pytesseract.image_to_string(Image.open(file))
                                          
        # Split it into a list based n end line char
        OCR = OCR.split('\n')
        
        # Get the index of any permanent text 
        ind = OCR.index("presented to")
                                          
        # Theres is a gap between two text, so the name will be after two indices of presented to
        if bool(OCR[ind+2]):
            name=OCR[7]
        # In some cases it's right after it
        else:
            name=OCR[ind+1]
        # Rename
        os.rename(file,"{} KWoC Mentor Certificate.jpg".format(name))

