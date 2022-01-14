#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import mediapipe as mp
import time
import TrackingModule as tm
import numpy as np
 

def thumb_closed():
    
    p4=np.array((lmList[4][1],lmList[4][2]))
    p5=np.array((lmList[5][1],lmList[5][2]))
    p0=np.array((lmList[0][1],lmList[0][2]))
    
    
    dist1 = np.linalg.norm(p4-p0)
    dist2 = np.linalg.norm(p5-p0)
    
    if dist1<dist2:
#         cv2.putText(img, "Thumb Closed", (400, 200), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (0, 0, 255), 2) 
        return True
    
    
    
def index_closed():
    
    p8=np.array((lmList[8][1],lmList[8][2]))
    p6=np.array((lmList[6][1],lmList[6][2]))
    p0=np.array((lmList[0][1],lmList[0][2]))
    
    
    dist1 = np.linalg.norm(p8-p0)
    dist2 = np.linalg.norm(p6-p0)
    
    if dist1<dist2:
#         cv2.putText(img, "Index Closed", (400, 400), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (0, 0, 255), 2)
        return True

    
def middle_closed():
    
    p12=np.array((lmList[12][1],lmList[12][2]))
    p10=np.array((lmList[10][1],lmList[10][2]))
    p0=np.array((lmList[0][1],lmList[0][2]))
    
    
    dist1 = np.linalg.norm(p12-p0)
    dist2 = np.linalg.norm(p10-p0)
    
    if dist1<dist2:
#         cv2.putText(img, "Middle Closed", (400, 350), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (0, 0, 255), 2)
        return True

    
def ring_closed():
    
    p16=np.array((lmList[16][1],lmList[16][2]))
    p14=np.array((lmList[14][1],lmList[14][2]))
    p0=np.array((lmList[0][1],lmList[0][2]))
    
    
    dist1 = np.linalg.norm(p16-p0)
    dist2 = np.linalg.norm(p14-p0)
    
    if dist1<dist2:
#         cv2.putText(img, "Ring Closed", (400, 300), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (0, 0, 255), 2) 
        return True
    

    
def pinky_closed():
    
    p20=np.array((lmList[20][1],lmList[20][2]))
    p18=np.array((lmList[18][1],lmList[18][2]))
    p0=np.array((lmList[0][1],lmList[0][2]))
    
    
    dist1 = np.linalg.norm(p20-p0)
    dist2 = np.linalg.norm(p18-p0)
    
    if dist1<dist2:
#         cv2.putText(img, "Pinky Closed", (400, 250), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (0, 0, 255), 2) 
        return True
    
    

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = tm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        
        
        
        if index_closed() and middle_closed() and ring_closed() and pinky_closed() and not thumb_closed():
            if lmList[4][2] < lmList[0][2]:
                cv2.putText(img, "Thumbs Up", (450, 200), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 0, 255), 2)
            else :
                cv2.putText(img, "Thumbs Down", (400, 200), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 0, 255), 2)
            
        if not(index_closed()) and not(middle_closed()) and ring_closed() and pinky_closed() and thumb_closed():
            cv2.putText(img, "V", (450, 200), cv2.FONT_HERSHEY_PLAIN, 4,
                (0, 0, 255), 2)
        if index_closed() and not(middle_closed()) and not ring_closed() and not pinky_closed() and thumb_closed():
            cv2.putText(img, "Okay", (450, 200), cv2.FONT_HERSHEY_PLAIN, 2,
                (0, 0, 255), 2)
            
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
 
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


# In[ ]:




