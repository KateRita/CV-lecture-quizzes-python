import cv2
import matplotlib.pyplot as plt

# Inspect image values
img = cv2.imread("images/dolphin.png")
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


cv2.waitKey(0)