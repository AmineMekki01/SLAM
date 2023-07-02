# importing libraries 
import cv2 
import pygame

from display import Display

display = Display(540, 960)


if __name__ == "__main__":
    video_cap = cv2.VideoCapture("./vids/fast_driving_car.mp4")
    test = Display(540, 960)
    # test that the video is beign read
    while video_cap.isOpened():

        ret, frame = video_cap.read()
        if ret == True:
            display.process_frame(frame)
        else:
            break 
    
video_cap.release()
cv2.destroyAllWindows()
    