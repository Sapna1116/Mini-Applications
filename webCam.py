#  pip install --user opencv-python

import cv2
from datetime import datetime as dt
import os

imgCapture = cv2.VideoCapture(0)

res = True
while res:
    timestamp = dt.now().strftime("%d-%m-%Y_%H-%M-%S")
    directory = 'Capture Image\Images Captured'

    if not os.path.exists(directory):
        os.makedirs(directory)

    imgName = f'{directory}/img_{timestamp}.jpg'

    ret, frame = imgCapture.read()
    cv2.imwrite(imgName, frame)

    print("Image Captured...")
    break  # Ensure the loop runs only once

# Display the captured image
cv2.imshow('Captured Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgCapture.release()
