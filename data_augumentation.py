import numpy as np
from PIL import Image
import skimage
from skimage import exposure
from skimage.transform import resize
import random
import matplotlib.pyplot as plt
import os


def data_augumentation(img):
    pick = random.randint(0, 1)
    if pick == 1:
        # random brightness
        brightness_factor = 1.0 + random.uniform(-0.15, 0.05)
        img = exposure.adjust_gamma(img, brightness_factor)
        
    pick = random.randint(0, 1)
    if pick == 1:
        # random low resolution
        img = skimage.transform.resize(img, (img.shape[0] // 4, img.shape[1] // 4), anti_aliasing=True)
        img = skimage.transform.resize(img, (img.shape[0] * 4, img.shape[1] * 4), anti_aliasing=True)
    
    img = np.clip(np.array(img)/255.0, 0, 1.0)
    return img


# do data augumentation for all folder
data_path = ''  # data path to labeled-data
root = os.path.join(data_path, 'labeled-data')
folders = []    # add all video file folder
for folder in folders:
    folder_path = os.path.join(root, folder)
    files = os.listdir(folder_path)
    img_names = [item for item in files if item[-4:] == '.png']
    
    # do data augumentation for each image
    for img_name in img_names:
        img_path = os.path.join(root, folder, img_name)
        img = Image.open(img_path)
        
        pick = random.randint(0, 1)
        if pick == 1:
            img_1 = np.array(img)/1.0
            img2 = data_augumentation(img_1)
            plt.imsave(img_path, img2)

