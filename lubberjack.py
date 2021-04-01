# pyscreenshot/examples/grabbox.py

"Grab the part of the screen"
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Controller
import numpy as np
import cv2
import time

print("starts in 5 secs")
time.sleep(3)
print("start")

keyboard = Controller()
keyR = Key.right
keyL = Key.left

# part of the screen
imL = ImageGrab.grab(bbox=(129, 221, 130, 222))  # X1,Y1,X2,Y2
piL = np.array(imL)

imR = ImageGrab.grab(bbox=(252, 221, 253, 222))  # X1,Y1,X2,Y2
piR = np.array(imR)

#cv2.imshow('left',piL)
#cv2.imshow('right',piR)

while True:
    imR = ImageGrab.grab(bbox=(252, 218, 253, 219))  # X1,Y1,X2,Y2
    piR = np.array(imR)
    
    if np.array_equal(piR, [[[160, 115, 61]]]):
        #print(piR)
        keyboard.press(keyL)
        keyboard.release(keyL)
        time.sleep(0.05)
        keyboard.press(keyL)
        keyboard.release(keyL)
    else:
#    if np.array_equal(piR, [[[160, 115, 61]]]):
        #print(piR)
        keyboard.press(keyR)
        keyboard.release(keyR)
        time.sleep(0.05)
        keyboard.press(keyR)
        keyboard.release(keyR)
        
    time.sleep(0.018)

#[[[212 247 254]]] blank
#[[[160 115  61]]] correct

#print(piL)
#print(piR)


cv2.waitKey()
