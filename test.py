#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
pat = [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1]
print(np.array(pat, float).reshape(1, len(pat)))
