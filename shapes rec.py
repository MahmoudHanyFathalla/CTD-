import cv2
import numpy as np
c_c=0
r_c=0
t_c=0
l_c=0
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("C:\\Users\\hp\\Desktop\\shaps\\img.jpg", cv2.IMREAD_GRAYSCALE)
imgg= cv2.imread("C:\\Users\\hp\\Desktop\\shaps\\imgg.JPG")
dim= (600,500)
imgrr = cv2.resize(imgg, dim, interpolation= cv2.INTER_LINEAR)
imgr = cv2.resize(img, dim, interpolation= cv2.INTER_LINEAR)

_, threshold = cv2.threshold(imgr, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
    cv2.drawContours(imgr, [approx], 0, (0,0,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(len(approx))
    
    if len(approx) == 3:
        cv2.putText(imgr, "Triangle", (x, y), font, .5, (0))
        t_c = t_c + 1
    elif len(approx) == 4:
        cv2.putText(imgr, "Rectangle", (x, y), font, .5, (0))
        r_c = r_c + 1
    elif len(approx) == 2:
        cv2.putText(imgr, "line", (x, y), font, .5, (0))
        l_c = l_c + 1
    elif len(approx) >= 6:
        cv2.putText(imgr, "Circle", (x, y), font, .5, (0))
        c_c = c_c + 1 
        
cv2.imshow("img", imgr)
cv2.imshow("Threshold", threshold)
cv2.putText(imgrr, f"{c_c}", (100, 90), font, 2, color=(0,0, 255),thickness=3)
cv2.putText(imgrr, f"{t_c}", (100, 190), font, 2, color=(0,0, 255),thickness=3)
cv2.putText(imgrr, f"{l_c}", (100, 310), font, 2, color=(0,0, 255),thickness=3)
cv2.putText(imgrr, f"{r_c-1}", (100, 450), font, 2, color=(0,0, 255),thickness=3)
cv2.imshow("imgg", imgrr)
cv2.waitKey(0)
cv2.destroyAllWindows()        