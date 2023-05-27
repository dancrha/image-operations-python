'''
Created on Oct. 21, 2022

@author: dancrha
References:

Addition and Subtraction:
https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-addition-and-subtraction/

Division:
https://www.geeksforgeeks.org/dividing-images-into-equal-parts-using-opencv-in-python/
https://www.askpython.com/python/examples/arithmetic-operations-on-images

Convolution:
https://www.geeksforgeeks.org/image-filtering-using-convolution-in-opencv/
'''

import cv2
import matplotlib.pyplot as plt

#Image Addition
image1 = cv2.imread('image1.png')
image2 = cv2.imread('image2.jpeg')
cv2.imshow('Addition - Image 1', image1)
cv2.imshow('Addition - Image 2', image2)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Image Addition Output', weightedSum)
    
#Image Subtraction
image3 = cv2.imread('image3.png')
image4 = cv2.imread('image4.png')
cv2.imshow('Subtraction - Image 1', image3)
cv2.imshow('Subtraction - Image 2', image4)
sub = cv2.subtract(image3, image4)
cv2.imshow('Image Subtraction Output', sub)


#Image Division - image split
image5 = cv2.imread('image5.jpeg')
cv2.imshow('Division - Original', image5)
h, w, channels = image5.shape
half = w//2
left_part = image5[:, :half]
right_part = image5[:, half:]

cv2.imshow('Division - Left part', left_part)
cv2.imshow('Division - Right part', right_part)

half2 = h//2

top = image5[:half2, :]
bottom = image5[half2:, :]

cv2.imshow('Division - Top', top)
cv2.imshow('Division - Bottom', bottom)

#Image division 2 - decreasing brightness
image8 = cv2.imread('division.png')
cv2.imshow('Division 2 - Original Image', image8)
div = cv2.divide(image8, 2)
cv2.imshow('Division 2 - Output Image', div)

#Image Convolution
img = cv2.imread('image7.jpeg')
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(3,3),sigmaX=0, sigmaY=0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gaussian_blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()




