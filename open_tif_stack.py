# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 12:01:23 2017

@author: jesse
"""

import cv2 as cv2
from skimage import io
import tkFileDialog
import Tkinter as tk
#import numpy as np

#video trackbar
def on_slider_move(event):
    index = cv2.getTrackbarPos('frame', 'test')
    cv2.imshow('test', im[index])

if __name__ == "__main__":
    #read in image
    root = tk.Tk()
    root.withdraw()
    filename = tkFileDialog.askopenfilename()
    root.destroy()
    
    im = io.imread(filename)
    
    #create the window and trackbar
    cv2.namedWindow('test')
    cv2.createTrackbar('frame', 'test', 0, im.shape[0] - 1, on_slider_move)
    cv2.imshow('test', im[0])
    
    #main loop
    while(1):
        #cv2.imshow('img', im[0])
        k = cv2.waitKey(33)
        if k == 27:
            break
        elif k == -1:
            continue

    #close openCV
    cv2.destroyAllWindows()