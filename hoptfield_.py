#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "philippe giraudeau <philippe@giraudeau.eu>"
__date__ = "01.10.13"
__usage__ = "Hopfield asynhrone"

"""
Etat poubelle. C'est parce que la partie croisé est plus importante que la partie principale.
"""
import numpy as np
import random


class Hopfield(object):
    """
    Classe créant un réseau de hopfield. L'apprentissage dans ce réseau fonctionne de manière bipolaire.
    TODO : Rajouter la possibilité de faire du binaire
    TODO : Rajouter une fonction calculant les points fixes de la matrice d'activation

    """

    def __init__(self, pattern, rate=1):
        self.pattern = pattern
        self.nb_neurones = len(self.pattern[0])
        self.nb_motifs = len(self.pattern)

        self.m = np.zeros((self.nb_neurones, self.nb_neurones)) # création matrice des poids
        self.matrix(rate)
        self.f = lambda x: self.active(x)

    def matrix(self, rate=1):
        """
        :param rate: ration d'apprentissage [1,-1]
        :return: None
        """

        for i in self.pattern:
            z = np.array(i, float).reshape(1, self.nb_neurones)
            #print(self.m)
            self.m += z * z.T
        self.m /= self.nb_neurones #divise et réaffecte le résultat dans m
        # self.m -= self.m.diagonal() * np.eye(self.nb_neurones)
        #print(self.m)

    def bruit(self, bruitage=0.1):
        """
        Bruite un pattern donné en entrée
        :param bruitage: pourcentage du bruit à installer dans le motif
        :return: le pattern bruité
        """
        assert isinstance
        bruitage = int(bruitage*10)
        while bruitage > 0:
            for i in range(len(self.pattern)):
                x = random.randrange(0,len(self.pattern[0]))
                if self.pattern[i][x] != 1 :
                    self.pattern[i][x] = 1
                elif self.BINARY == True:
                    self.pattern[i][x] = 0
                else:
                    self.pattern[i][x] = -1
            bruitage -= 1
        print(self.pattern)

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


    def calcEnergie(self, matrice, pattern):
        """
        Calcul l'energie
        :param matrice: np.array, matrice d'activation de hopfield
        :param pattern: np.array, vecteur d'entré
        :return: energie: double, l'energie pour le pattern
        """


    def vecActiv(self,f, matrice):
        """
        Applique la fonction d'activation sur le vecteur
        :param f:
        :param matrice:
        :return:
        """
        o = matrice.flat
        return np.array(list(map(f, o))).reshape(matrice.shape)


    def asyn(self,m, y, i):
        """
        :param m: matrice de Hopfield
        :param y: donnee à traiter
        :param i: index a mettre à jour
        :return: x:
        """

        x = self.vecActiv(self.f, np.dot(y, m[..., i]))
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
        """
        Methode asynchrone de restitution des données
        :return: None
        """
        for i in self.pattern:
            pattern = np.array(i, float)
            for j in range(self.nb_neurones):
                o = self.asyn(self.m, pattern, j)
                pattern[j] = o
            print("le pattern ", i, "=> ", self.stable(i, pattern))


    def stable(self,data,pat):
        """
        Détermine si la valeur de sortie correspond à la valeur stockée en mémoire
        :param data: valeur d'entrée
        :param pat: valeur stockée
        :return:
        """

        if np.all(np.array(data, float) == pat):
           return "100.0"
        else:
            return self.matchTo(pat, data)


    def pas(self):
        """
        Fonction qui prend en argument une matrice d'activation du réseau de hopfield
        :return:
        """
        for _ in self.pattern:

            y = np.array(_)
            out = np.dot(y, self.m) #multiplication de matrice
            print("input", y, end=',')
            print("sortie", out, "=====>", np.sign(out), end=',')
            if np.all(np.sign(out) == np.sign(y)):
                print('stable')
            else:
                print('non stable')

    def matchTo(self,sortie, pat):
        """
        Renvoie le pourcentage de match d'un pattern entrée dans la matrice
        d'activation.
        :param sortie: le pattern de sortie
        :param pat: Le pattern entrée dans la matrice
        :return: pourcentage de reconnaissance. pat == 100, Stable. pat < 100, Non Stable
        """
        match = 0
        for i in range(len(pat)):
            if sortie[i] == pat[i]:
                match +=1
        match = (match/len(pat))*100
        return match
