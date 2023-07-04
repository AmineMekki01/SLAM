import cv2 
import numpy as np

class FeatureExtractor(object):

    def __init__(self):
        self.orb = cv2.ORB_create(nfeatures=100)
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        self.last = None
        
    def extract(self, img):
        # detection
        feats =  cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        
        # extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)
        
        # matching 
        ret = []
        if self.last is not None:        
            matches = self.bf.knnMatch(des, self.last['des'], k=2)
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    ret.append((kps[m.queryIdx], self.last['kps'][m.trainIdx]))
        
        # return
        self.last = {'kps' : kps, 'des' : des} 
        
        return ret