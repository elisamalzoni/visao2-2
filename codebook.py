import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from PIL import Image


class Codeword():
    def __init__(self, v, aux):
        self.v = v
        self.aux = aux
    
    # def R(self):
    #     return self.v[0]

    # def G(self):
    #     return self.v[1]
    
    # def B(self):
    #     return self.v[2]
        
    # def min_brightness(self):  #min brightness of all pixels assigned to this codeword 
    #     return self.aux[0]

    # def max_brightness(self):  #max brightness of all pixels assigned to this codeword 
    #     return self.aux[1]

    # def frequency(self):       #frequency with which the codeword has ocurred f
    #     return self.aux[2]

    # def mnrl(self):            #lambda, maximum negative run-length, longest interval during the 
    #     return self.aux[3]     #training period that the codeword has NOT recurred

    # def p(self):               #first access time that the codeword has occurred
    #     return self.aux[4]
    
    # def q(self):               #last access time that the codeword has occurred
    #     return self.aux[5]
    
def colordist(x, v): #um pixel, codeword
    normaxt2 = ((x[0]**2) + (x[1]**2) + (x[2]**2))
    normavi2 = v[0]**2 + v[1]**2 +v[2]**2
    tupxtvi2 = (v[0]*x[0] + v[1]*x[1] + v[2]*x[2])**2
    if normavi2 == 0:
        p2 = 0
    else:
        p2 = (tupxtvi2/normavi2)

    return math.sqrt(abs((normaxt2) - (p2)))

# Ilow Ihi 

def brightness(xt, Imax, Imin):
    alpha = 0.4
    beta = 1.1
    Ilow = alpha* Imax
    Ihi = min(beta*Imax, Imin/alpha)
    normaxt= math.sqrt(xt[0]**2, xt[1]**2, xt[2]**2)
    if (Ilow <= normaxt and normaxt <= Ihi):
        return True
    return False


# def codebook(training_seq):

## converter img pra float logo depois de ler

# C = [[] for i in range(img.shape[0]*img.shape[1])] ## nd array a matriz de fora
# L = 0


# N qtd de imagens
N = 1
# img = Image.open("00000001.jpg")
img = cv2.imread("00000001.jpg")
print(img.shape)

C =[]
for i in range(img.shape[0]):
    C.append([])
    for j in range (img.shape[1]):
        C[i].append([])



for t in range(1, N+1):
    
    for linha in range(img.shape[0]):
        for coluna in range(img.shape[1]):
            xt = img[linha, coluna, :]
            I = math.sqrt(xt[0]**2 + xt[1]**2 + xt[2]**2)
            match = False
            for cw in C[linha][coluna]:
                if (colordist(xt, cw.v) <= E1) and (brightness(xt, cw.aux[0],cw.aux[1])):
                    #atuliza codeword
                    fm = cw.v[2]
                    Rm = (fm*cw.v[0] + xt[0])/ (fm + 1)
                    Gm = (fm*cw.v[1] + xt[1])/ (fm + 1)
                    Bm = (fm*cw.v[2] + xt[2])/ (fm + 1)
                    cw.v = (Rm, Gm, Bm)
                    cw.aux[0] = min(I, cw.aux[0])
                    cw.aux[1] = max(I, cw.aux[1])
                    cw.aux[2] = fm + 1
                    cw.aux[3] = max(cw.aux[3], t - cw.aux[5])
                    cw.aux[4] = cw.aux[4] ### ???
                    cw.aux[5] = t
                    match = True

                    break

            if not match:
                newcw = Codeword(xt, [I, I, 1, t-1, t, t])
                
                C[linha][coluna].append(newcw)

    #atuliza lambda com for nos codewords
    for linha in range(img.shape[0]):
        for coluna in range(img.shape[1]):
            for cw in C[linha][coluna]:
                cw.aux[3] = max(cw.aux[3],(N - cw.aux[5] + cw.aux[4] - 1))

print(C)