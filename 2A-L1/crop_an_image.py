import cv2

# Crop an image
img = cv2.imread('images/bicycle.png');
cv2.imshow('Bicycle', img);


print(img.shape);  # check size

cropped = img[110:310, 10:160];
cv2.imshow('Cropped', cropped);

# TODO: Find out cropped image size

cv2.waitKey(0);