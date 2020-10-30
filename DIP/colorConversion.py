"""Convert and display image in different color"""

import cv2
image=cv2.imread("image2.png")
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("RGB",rgb)
cv2.imshow("Grey",grey)
cv2.imshow("HSV",hsv)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()

