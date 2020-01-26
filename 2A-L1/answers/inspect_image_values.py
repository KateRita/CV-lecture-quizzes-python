import cv2
import matplotlib.pyplot as plt

# Inspect image values
img = cv2.imread("../images/dolphin.png")
cv2.imshow('Dolphin', img)
print(img.shape)

###
# sample code from video
# single pixel
print(img[50,100])

# entire row
print(img[50, :, 0])

plt.plot(img[50, :, 0])
plt.show()



# TODO: Extract a 2D slice between rows 101 to 103 and columns 201 to 203 (inclusive)
#NOTE: the code to extract rows 101 to 103 and columns 201 to 203 is:
slice = img[101:104, 201:204, 0]

# However, to get the same cell values that are displayed in the video, you need to subtract one from each index
# because python indexes arrays starting with 0, and matlab indexes starting with 1
slice = img[100:103, 200:203, 0]
print(slice)

cv2.waitKey(0)
