# pip install --user pyautogui

import pyautogui as pag
import time
from datetime import datetime as dt
import os
import tkinter as tk

def screenShot():
    timestamp = dt.now().strftime("%d-%m-%Y_%H-%M-%S")
    directory = 'Capture ScreenShot\Screenshots Captured'
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    imgName = f'{directory}/img_{timestamp}.jpg'
    # time.sleep(2)
    img = pag.screenshot(imgName)
    img.show()

# screenShot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Creating buttons
button = tk.Button(frame, text = "Take Screenshot", command = screenShot)
button.pack(side=tk.LEFT)

# can't use 'quit' since its a keyword. thus using 'close' 
close = tk.Button(frame, text = "QUIT", command = quit)
close.pack(side=tk.LEFT)

root.mainloop()