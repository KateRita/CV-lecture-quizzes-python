import cv2

# Crop an image
img = cv2.imread('../images/bicycle.png');
cv2.imshow('Bicycle', img);


print(img.shape);  # check size

cropped = img[110:310, 10:160];
cv2.imshow('Cropped', cropped);

# TODO: Find out cropped image size
#note: in python row/column selection excludes the last pixel.
# so the size in matlab is: (201, 151) and in python it's (200, 150) with the same input.
print(cropped.shape)

cv2.waitKey(0);
