import cv2
 
img = cv2.imread('C:\\Users\\Admin\\Desktop\\cudis\\web\\cudis\\static\\images\\rgk.jpg', cv2.IMREAD_UNCHANGED)

#cv2.imshow("img",img)
 
#print('Original Dimensions : ',img.shape())
 
scale_percent = 60 # percent of original size
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
dim = (300,400)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

 
#print('Resized Dimensions : ',resized.shape)
 
#cv2.imshow("Resized image", resized)
cv2.imwrite('C:\\Users\\Admin\\Desktop\\cudis\\web\\cudis\\static\\images\\rgk_resized.jpg',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()