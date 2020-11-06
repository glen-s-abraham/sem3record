import numpy as np
import cv2

img1=np.zeros([500,500,3],np.uint8)
img1[255,:]=255
img1[:,255]=255

cv2.imshow("image",img1)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
