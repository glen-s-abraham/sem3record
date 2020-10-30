"""Split and merge color channels"""
import cv2
image=cv2.imread("image2.png")
b,g,r=cv2.split(image)

cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)

merged=cv2.merge((r,g,b))
cv2.imshow("Merged",merged)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
