import cv2



# Load the image

image = cv2.imread('example.jpg')



# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




# Resize the resized graysacle image to 224*224

resized_image = cv2.resize(gray_image,(224,224)) 



#Display the resized grayscale image in a single window

cv2.imshow('processed image',resized_image)



#Wait for a key press
Key = cv2.waitKey(0) # wait indefinitely for a key press




#check if the "s"key was pressed (ASCII for 's' is 83)

if key == ord('s'):

    #save the processed image when 's' is pressed

    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print("Image saved as grayscale_resized_image.jpg")


else:
    print("image not saved")





#close the window
cv2.destroyeAllWindows() 



#print processed image properties

print(f"Processed Image Dimensions: {resized_image.shape}")
        