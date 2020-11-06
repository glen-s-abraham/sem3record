import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)/25

img=cv2.imread('noisy.png')

#convolution filtering
convolution=cv2.filter2D(img,-1,kernel)

#blur
blur=cv2.blur(img,(5,5))

#gaussian
gaussian=cv2.GaussianBlur(img,(5,5),2)

#median
median=cv2.medianBlur(img,5)

#bilateral
bilateral=cv2.bilateralFilter(img,5,75,75)

cv2.imshow("Noisy",img)
#cv2.imshow("Convolution",convolution)
#cv2.imshow("blur",blur)
#cv2.imshow("gaussian",gaussian)
#cv2.imshow("median",median)
cv2.imshow("bilateral",bilateral)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()