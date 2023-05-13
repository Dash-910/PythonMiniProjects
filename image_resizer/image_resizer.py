# pip install opencv-python 

import cv2

# percent by which the image is created
scale_percent = 50

source = "img1.png"
destination = "newImg1.png"

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
print(src)
cv2.imshow("title",src)

# calculate the 50 percent of orginal dimensions
width = int(src.shape[1] * scale_percent /100)
height = int(src.shape[0] * scale_percent/100)

# resize image
output = cv2.resize(src,(width,height))

cv2.imwrite(destination,output)
cv2.waitKey(0)


