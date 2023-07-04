# importing libraries 
import cv2 
import pygame
import numpy as np

from display import Display
from extractor import FeatureExtractor

display = Display(540, 960)

HEIGHT = 540
WIDTH = 960
    
featExt = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img,(display.width ,display.height))
    matches = featExt.extract(img)
    if matches is None:
        return 
    
    for pt1, pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1.pt)
        u2, v2 = map(lambda x: int(round(x)), pt2.pt)
        
        cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1,v1), (u2, v2), color=(255,0,0))
        
 
    display.plot_vid(img)
    
if __name__ == "__main__":
    video_cap = cv2.VideoCapture("./vids/fast_driving_car.mp4")
    test = Display(540, 960)
    # test that the video is beign read
    while video_cap.isOpened():

        ret, frame = video_cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break 
        
    video_cap.release()
    cv2.destroyAllWindows()
        
    



# dy = img.shape[0]//self.GY
        # dx = img.shape[1]//self.GX
        # akp = []
        # for ry in range(0, img.shape[0], dy):
        #     for rx in range(0, img.shape[1], dx):
                
        #         img_chunk = img[ry:ry+dy, rx:rx+dx]
        #         # print(img_chunk.shape)
        #         kp = self.orb.detect(img_chunk, None)
        #         for p in kp:
        #             p.pt = (p.pt[0] + rx, p.pt[1] + ry)
        #             akp.append(p)
        
        # return akp
        