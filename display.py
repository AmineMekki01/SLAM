import pygame
import cv2

class Display(object):
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
    
    def process_frame(self, img):
        img = cv2.resize(img,(self.width ,self.height))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(img_rgb.swapaxes(0,1) ).convert()
        self.screen.blit(surf , (0,0))
        pygame.display.flip()

        