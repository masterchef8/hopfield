#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import pylab as pl
import matplotlib.cm as cm

def int2B(pat, binary=True):
    _ = np.array(pat, float)
    for i in range(len(_)):
        for j in range(len(_[i])):
            if binary:
                if pat[i][j] > 130:
                    _[i][j] = 1
                else:
                    _[i][j] = 0
            else:
                if j > 75:
                    _[i][j] = 1
                else:
                    _[i][j] = -1
    r = np.array(_, float).reshape(1,54000).flatten()
    return r


un = np.array(Image.open('data/picture/1.jpg').convert('L'))
deux = np.array(Image.open('data/picture/2.jpg').convert('L'))
trois = np.array(Image.open('data/picture/3.jpg').convert('L'))
quatre = np.array(Image.open('data/picture/4.jpg').convert('L'))


visages = [int2B(un), int2B(deux), int2B(trois), int2B(quatre)]