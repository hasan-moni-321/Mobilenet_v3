from mobilenet_v3 import *
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    result, object_info = get_objects(img, 0.45, 0.2, objects=['cup','mouse'])
    print(object_info)

    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




