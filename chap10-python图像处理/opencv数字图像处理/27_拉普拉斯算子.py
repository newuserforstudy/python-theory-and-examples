import cv2
image = cv2.imread("images/3.jpg")
src = cv2.GaussianBlur(image,(0,0,),1)

dst = cv2.Laplacian(src,cv2.CV_32F,ksize=3,delta=127)
dst = cv2.convertScaleAbs(dst)

cv2.imshow("laplacian",dst)
cv2.waitKey()