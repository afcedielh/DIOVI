import asyncio
from ObjectDetectorModule import *
from SpechModule import *

text_to_voice("Iniciando sistema DIOVI, por favor espera.")

cap = cv2.VideoCapture('C:/Users/User/Downloads/1.mp4')
out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)
while True:
    success, img = cap.read()
    result, objectInfo = getObjects(img, True, 0.2, objects=['umbrella',
                                                             'street sign',
                                                             'bicycle',
                                                             'car',
                                                             'motorcycle',
                                                             'traffic light'])
    if len(objectInfo) > 0:
        # text_to_voice(objectInfo[0][1])
        print(objectInfo)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
