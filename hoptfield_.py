#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "philippe giraudeau <philippe@giraudeau.eu>, camille el habr "
__date__ = "01.10.13"
__usage__ = "Hopfield asynhrone"

"""
Etat poubelle. C'est parce que la partie croisé est plus importante que la partie principale.
"""
import numpy as np


class Hopfield(object):

    def __init__(self, pattern, rate=1):
        self.pattern = pattern
        self.nb_neurones = len(self.pattern[0])
        self.nb_motifs = len(self.pattern)

        self.m = np.zeros((self.nb_neurones, self.nb_neurones)) # création matrice des poids
        self.matrix(rate)
        self.f = lambda x: self.active(x)

    def matrix(self,rate=1):
        for i in self.pattern:
            z = np.array(i, float).reshape(1, self.nb_neurones)
            print(self.m)
            self.m += z * z.T
        self.m /= self.nb_neurones #divise et réaffecte le résultat dans m
        # self.m -= self.m.diagonal() * np.eye(self.nb_neurones)
        print(self.m)

    """
    * Permet de faire apprendre ou désaprendre à motif seul
    """
    def learn(self,pat,rate=1.):
        """
            m est la matrice courante, pat est le pattern a apprendre
            rate: facteur
            rate < 0 : oubli
        """
        assert -1 <= rate <= 1, "%s in [-1 .. 1]" % rate
        _sz = len(pat)
        _p = np.array(pat, float).reshape(1, _sz)# crée une matrice de float
        _mp = p * p.T

        _mp = _mp / _sz  # pour rester dans des petites valeurs
        _mp -= _mp.diagonal() * np.eye(_sz)
        _mp *= rate

        self.m += _mp


    def map_fun(self,f, matrice):
        """ applique f sur les éléments de la matrice """
        o = matrice.flat
        return np.array(list(map(f, o))).reshape(matrice.shape)


    def asyn(self,m, y, i):
        """
        * m : matrice de Hopfield
        * y : donnee à traiter
        * i : index a mettre à jour
        """
        x = self.map_fun(self.f, np.dot(y, m[..., i]))
        return x
    def active(self,x):
        """
        fonction de seuillage
        si > theta : 1
        si < theta : min
        sinon theta
        """
        if x > 0: return 1
        if x == 0: return 0
        return -1

    def evoluer(self):
        for i in self.pattern:
            pattern = np.array(i, float)
            print("data", pattern)
            for j in range(self.nb_neurones):
                o = self.asyn(self.m, pattern, j)
                pattern[j] = o
                print(i[j], '->', o)
            self.stable(i, pattern)
        print("fin asynchrone")
        print("=" * 20)


    def stable(self,data,pat):
        if np.all(np.array(data, float) == pat):
            print("Stable")
            return True
        else:
            print("Non Stable")
            return False


    def pas(self):
        """
        Fonction qui prend en argument une matrice d'activation du réseau de hopfield
        """
        for _ in self.pattern:
            """
            y : les inputs
            out : la multiplication
            """
            y = np.array(_)
            out = np.dot(y, self.m) #multiplication de matrice
            print("input", y, end=',')
            print("sortie", out, "=====>", np.sign(out), end=',')
            if np.all(np.sign(out) == np.sign(y)):
                print('stable')
            else:
                print('non stable')







