#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "philippe giraudeau <philippe@giraudeau.eu>"
__date__ = "16.11.13"
__usage__ = "Hopfield asynhrone"

import hoptfield_ as h
import numpy as np
import face as f
zero = [0, 1, 1, 0,
        1, 0, 0, 1,
        1, 0, 0, 1,
        0, 1, 1, 0]

one = [1, 1, 1, 1,
       0, 0, 0, 1,
       0, 0, 0, 1,
       0, 0, 0, 1]

two = [1, 1, 1, 1,
       0, 0, 1, 0,
       0, 1, 0, 0,
       1, 1, 1, 1]

three = [1, 1, 1, 1,
         0, 0, 1, 0,
         0, 0, 1, 0,
         1, 1, 1, 1]

four = [1, 0, 0, 0,
        1, 0, 0, 0,
        1, 1, 1, 1,
        0, 0, 1, 0]

five = [1, 1, 1, 1,
        1, 0, 0, 0,
        0, 1, 0, 0,
        1, 1, 1, 1]

six = [1, 1, 1, 1,
       1, 0, 0, 0,
       1, 1, 1, 1,
       1, 1, 1, 1]

seven = [1, 1, 1, 1,
         0, 0, 0, 1,
         0, 1, 1, 1,
         0, 0, 0, 1]

eight = [1, 1, 1, 1,
         0, 1, 1, 0,
         1, 0, 0, 1,
         1, 1, 1, 1]

nine = [1, 1, 1, 1,
        1, 1, 1, 1,
        0, 0, 0, 1,
        1, 1, 1, 1]

zeroBis = [-1, 1, 1, -1,
           1, -1, -1, 1,
           1, -1, -1, 1,
           -1, 1, 1, -1]

un = [1, 1, 1, 1,
      -1, -1, -1, 1,
      -1, -1, -1, 1,
      -1, -1, -1, 1]

deux = [1, 1, 1, 1,
        -1, -1, 1, -1,
        -1, 1, -1, -1,
        1, 1, 1, 1]

trois = [1, 1, 1, 1,
         -1, -1, 1, -1,
         -1, -1, 1, -1,
         1, 1, 1, 1]

quatre = [1, -1, -1, -1,
          1, -1, -1, -1,
          1, 1, 1, 1,
          -1, -1, 1, -1]

cinq = [1, 1, 1, 1,
        1, -1, -1, -1,
        -1, 1, -1, -1,
        1, 1, 1, 1]

six_ = [1, 1, 1, 1,
       1, -1, -1, -1,
       1, 1, 1, 1,
       1, 1, 1, 1]

sept = [1, 1, 1, 1,
        -1, -1, -1, 1,
        -1, 1, 1, 1,
        -1, -1, -1, 1]

huit = [1, 1, 1, 1,
        -1, 1, 1, -1,
        1, -1, -1, 1,
        1, 1, 1, 1]

neuf = [1, 1, 1, 1,
        1, 1, 1, 1,
        -1, -1, -1, 1,
        1, 1, 1, 1]

if __name__ == '__main__':
    bipolaireBig = [[-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1]]

    binaireBig = [[0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]

    binaire = [zero, one, two, three, four, five, six, seven, eight, nine]

    bipolaire = [zeroBis, un, deux, trois, quatre, cinq, six_, sept, huit, neuf]

    hopBipV = h.Hopfield(bipolaireBig)
    hop = h.Hopfield(bipolaire)


   #hopBipBig = h.Hopfield(bipolaire)

    print("------------------BIP-------------------")
    #hopBipV.evoluer()

    hop.evoluer()
    hop.learn(np.array(bipolaire), -1)
    hop.evoluer()
    print("------------------BIPBIG-------------------")
    #hopBipBig.evoluer()
