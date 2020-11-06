img1=np.zeros([500,500,3],np.uint8)

cv2.putText(img1,"Opencv",(10,10))
cv2.imshow("image",img1)

if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()