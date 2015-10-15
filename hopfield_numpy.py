#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "mmc <marc.corsini@u-bordeaux2.fr>"
__date__ = "01.10.13"
__usage__ = "Hopfield synchrone"

import numpy as np
"""

datas : C'est les données à apprendre.
lng : C'est la longueur des données à apprendre.
m : Une matrice de la taille des données.
Matrix : La fonction matrice va remplir la matrice d'activation m
"""

# les données c'est du n'importe quoi
datas = [[-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1]]

#lng prend la mesure
lng = len(datas[0])

# creation et initialisation de la matrice
m = np.zeros((lng, lng))


def matrix(datas, m):
    for _ in datas:
        z = np.array(_).reshape(1, lng)
        m += z * z.T
    m /= lng #divise et réaffecte le résultat dans m



def pas(m):
    """
    Fonction qui prend en argument une matrice d'activation du réseau de hopfield
    """
    for _ in datas:
        """
        y : les inputs
        out : la multiplication
        """
        y = np.array(_)
        out = np.dot(y, m) #multiplication de matrice
        print("input", y, end=',')
        print("sortie", out, "=====>", np.sign(out), end=',')
        if np.all(np.sign(out) == np.sign(y)):
            print('stable')
        else:
            print('non stable')

def bruit():
    pass


matrix(datas, m)
print(m)
pas(m)
