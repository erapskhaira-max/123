import cv2



#Load the image
image = cv2.imread('image.jpg')




#resize the window to a specific size without resizing the image
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image',800,500) #set the window size to 800*500(width*height)

#Display the image in the resized window
cv2.imshow('Loaded Image',image)
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() # close the window

#Print image properties
print(f"Image Dimensions: {image.shape}") # Height, width, channels
