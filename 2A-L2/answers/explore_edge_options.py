import cv2
import numpy as np

# Explore edge options
img = cv2.imread('../images/fall-leaves.png')
cv2.imshow('Img', img)

# Create a Gaussian filter
filter_size = 40
filter_sigma = 2

# OpenCV does not have a fspecial type of function. Instead we will cv2.getGaussianKernel
# to generate a Gaussian kernel.
filter_kernel = cv2.getGaussianKernel(filter_size, filter_sigma)

# This however generates a 1D kernel and we want a 2D that is of shape (filter_size, filter_size)
# To achieve this we multiply this array by its transpose
filter_kernel = filter_kernel * filter_kernel.T

# Apply it, specifying an edge parameter (try different parameters)

filtered_image = cv2.filter2D(img, -1, filter_kernel, borderType=cv2.BORDER_REPLICATE)
cv2.imshow('replicate', filtered_image)


filtered_image = cv2.filter2D(img, -1, filter_kernel, borderType=cv2.BORDER_REFLECT)
cv2.imshow('reflect', filtered_image)

# filtered_image = cv2.filter2D(img, -1, filter_kernel, borderType=cv2.BORDER_WRAP)
# cv2.imshow('wrap', filtered_image)

cv2.waitKey(0)