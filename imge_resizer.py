#install and import pillow
#open the imge we want to resize
#print the curren size of the image
#specify the size we want to change it to
#save the new resized image

from PIL import Image
import os
import cv2

def resize_img(size1,size2):
    image = Image.open("fantasia 2.jpg")

    print(f"Current size : {image.size}" )

    resized_image = image.resize((size1,size2))

    resized_image.save("fantasia1" + str(size1) + ".jpg")

size1 = int(input("Enter width : "))
size2 = int(input("Enter length : "))
resize_img = (size1,size2)


#still under review
