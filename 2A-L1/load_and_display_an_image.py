import cv2

# load and display an image
img = cv2.imread("images/dolphin.png")
cv2.imshow('Dolphin', img)
cv2.waitKey(0)

# image size
print(img.shape)

# image class or data type
print(type(img));
