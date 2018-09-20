import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time

class Codeword():
    def __init__(self, RGBvector, aux):
        RGBvector.self = RGBvector
        aux.self = aux
    
    def R(self):
        return self.RGBvector[0]

    def G(self):
        return self.RGBvector[1]
    
    def B(self):
        return self.RGBvector[2]
        
    def min_brightness(self):  #min brightness of all pixels assigned to this codeword Ǐ
        return self.aux[0]

    def max_brightness(self):  #max brightness of all pixels assigned to this codeword Î
        return self.aux[1]

    def frequency(self):       #frequency with which the codeword has ocurred f
        return self.aux[2]

    def mnrl(self):            #lambda, maximum negative run-length, longest interval during the 
        return self.aux[3]     #training period that the codeword has NOT recurred

    def p(self):               #first access time that the codeword has occurred
        return self.aux[4]
    
    def q(self):               #last access time that the codeword has occurred
        return self.aux[5]
    

def colordist(xt, cw): #um pixel, codeword
    normaxt2 = ((xt[0]**2) + (xt[1]**2) + (xt[2]**2))
    normavi2 = cw.R()**2 + cw.G()**2 +cw.B()**2
    tupxtvi2 = (cw.R()*xt[0] + cw.G()*xt[1] + cw.B()*xt[2])**2
    p2 = (tupxtvi2/normavi2)
    return math.sqrt((normaxt2) - (p2))

## Ilow Ihi 

def brightness(I,(min, max), xt):
    normaxt = math.sqrt(xt.R() + xt.G() + xt.B())
    if (Ilow <= normaxt and normaxt <= Ihi):
        return True
    return False


def codebook(training_seq):
    for i in len(training_seq):
        x = training_seq[i]
        I = math.sqrt((x[0]**2) + (x[1]**2) + (x[2]**2))
