import cv2
import numpy as np
import random
import urllib.request
import json

with open("filename_to_url_map.json", 'r') as file:
    filename_to_url_map = json.load(file)

class ImageProcessor:
    def __init__(self, image_url):
        self.image_url = image_url
        self.url_not_found=False        
        try:
            resp = urllib.request.urlopen(image_url)
            img = np.asarray(bytearray(resp.read()), dtype="uint8")
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            self.image = img
        except:
            self.url_not_found=True
            
        
        
        
    def url_not_found(self):
        return self.url_not_found
    
    def adjust_contrast(self, contrast_factor):
        self.image = cv2.convertScaleAbs(self.image, alpha=contrast_factor, beta=0)

    def resize_image(self, width=None, height=None):
        if width is not None and height is not None:
            self.image = cv2.resize(self.image, (width, height))
        elif width is not None:
            self.image = cv2.resize(self.image, (width, int(self.image.shape[0] * (width / self.image.shape[1]))))
        elif height is not None:
            self.image = cv2.resize(self.image, (int(self.image.shape[1] * (height / self.image.shape[0])), height))

    def random_flip(self):
        flip_code = random.randint(-1, 1)  # -1 for horizontal flip, 0 for vertical flip, 1 for horizontal and vertical flip
        self.image = cv2.flip(self.image, flip_code)

    def adjust_brightness(self, brightness_factor):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * brightness_factor, 0, 255)
        self.image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def adjust_exposure(self, exposure_factor):
        self.image = cv2.convertScaleAbs(self.image, alpha=exposure_factor, beta=0)
    
    def save_image(self):
        path='./Image_Dataset/'
        cv2.imwrite(path+filename_to_url_map[self.image_url], self.image)  
        
    def display_image(self):
        cv2.imshow("Pre-processed Image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def processing_image(self):
        self.adjust_contrast(1.5)  # Increase contrast
        self.resize_image(width=500)  # Resize image to width 300 pixels
        self.random_flip()  # Random horizontal or vertical flip
        self.adjust_brightness(1.2)  # Increase brightness
        self.adjust_exposure(1.2)  # Increase exposure
        self.save_image()
        # self.display_image()



 


