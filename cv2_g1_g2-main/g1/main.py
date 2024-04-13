import cv2


img = cv2.imread("cv2_g1_g2/1.jpg")
img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2))
cv2.imshow("Name cat", img)

cv2.waitKey(0)

