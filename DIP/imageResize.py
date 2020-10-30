"""Resize an image"""
import cv2
image=cv2.imread("parrot.jpg")
originalheight,originalwidth,originaldepth=image.shape

print("Original width:",originalwidth,"Original Height:",originalheight)
width=int(input("Enter new Width:"))
height=int(input("Enter new Height:"))


scaledimage=cv2.resize(image,(int(width),int(height)))
cv2.imshow("Original",image)
cv2.imshow("Resized",scaledimage)


if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
