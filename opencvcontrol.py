
import cv2
import numpy as np

import time 


cam = cv2.VideoCapture(0)


detector = cv2.QRCodeDetector()



while True:
    succesful, image = cam.read()

    start = time.perf_counter()

    value, points, qrcode = detector.detectAndDecode(image)

    if value == "":
         cv2.putText(image, "Searching for QR code...", (720, 1000), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    if value != "":
        x1 = points[0][0][0]
        y1 = points[0][0][1]
        x2 = points[0][2][0]
        y2 = points[0][2][1]

        x_center = (x2 - x1) / 2 + x1
        y_center = (y2 - y1) / 2 + y1

        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 5)
        cv2.circle(image, (int(x_center), int(y_center)), 10, (0, 0, 255), -1)
        cv2.putText(image, value, (20, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (200,0,255), 1)

       

     
    if not succesful:
        print("could not capture image from the camera")
        
        break

    


    cv2.imshow("QR Code Scanner", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

 
