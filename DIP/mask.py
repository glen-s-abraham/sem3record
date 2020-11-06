import numpy as np
import cv2

img1=np.zeros([500,500,3],np.uint8)
img2=np.zeros([500,500,3],np.uint8)
img2[255:]=255

cv2.imshow("image 1",img1)
cv2.imshow("image 2",img2)

or_op=cv2.bitwise_or(img1,img2)
and_op=cv2.bitwise_and(img1,img2)

cv2.imshow("OR",or_op)
cv2.imshow("AND",and_op)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
