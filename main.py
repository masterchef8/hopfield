#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "philippe giraudeau <philippe@giraudeau.eu>"
__date__ = "16.11.13"
__usage__ = "Hopfield asynhrone"

import hoptfield_ as h
import numpy as np

bipolaire = [[-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1],
        [1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1]]

hop = h.Hopfield(bipolaire)
hop.evoluer()