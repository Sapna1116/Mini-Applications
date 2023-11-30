# import cv2
# from datetime import datetime as dt
# import os
 
# img = cv2.imread("Image To Sketch\Images To Be Converted Into Sketches\img.jpg")
# grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# invert_img = cv2.bitwise_not(grey_img)
# blur_img = cv2.GaussianBlur(invert_img, (21,21), 0)
# inverted_blur_img = cv2.bitwise_not(blur_img)
# sketch_img = cv2.divide(grey_img, inverted_blur_img, scale = 256.0)

# timestamp = dt.now().strftime("%d-%m-%Y_%H-%M-%S")
# directory = 'Image To Sketch\Sketches Created'

# if not os.path.exists(directory):
#     os.makedirs(directory)

# img_name = f'{directory}/sketch_for_{timestamp}.jpg'

# cv2.imwrite(img_name, sketch_img)


import cv2
from datetime import datetime as dt
import os

# Path to the input image
input_image_path = "Image To Sketch\Images To Be Converted Into Sketches\img.jpg"

# Read the input image
img = cv2.imread(input_image_path)

# Convert the image to grayscale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert_img = cv2.bitwise_not(grey_img)

# Apply Gaussian blur
blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)

# Invert the blurred image
inverted_blur_img = cv2.bitwise_not(blur_img)

# Create the sketch by dividing the grayscale image by the inverted blurred image
sketch_img = cv2.divide(grey_img, inverted_blur_img, scale=256.0)

# Get the name of the entered image without the path and extension
input_image_name = os.path.splitext(os.path.basename(input_image_path))[0]

# Create a timestamp for the output file name
timestamp = dt.now().strftime("%d-%m-%Y_%H-%M-%S")

# Directory to save the sketches
directory = 'Image To Sketch\Sketches Created'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Construct the output image name with the desired format
output_img_name = f'{directory}/sketch_for_{input_image_name}_{timestamp}.jpg'

# Save the sketch image
cv2.imwrite(output_img_name, sketch_img)

print(f"Sketch_Image saved as: {os.path.basename(output_img_name)}")

