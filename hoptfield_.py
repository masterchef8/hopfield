#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "philippe giraudeau <philippe@giraudeau.eu>, camille el habr "
__date__ = "01.10.13"
__usage__ = "Hopfield asynhrone"

"""
Etat poubelle. C'est parce que la partie croisé est plus importante que la partie principale.
"""
import numpy as np

# Recall a pattern (synchronous)
def recall(W, patterns, steps=5):
    sgn = np.vectorize(lambda x: -1 if x < 0 else +1)
    for _ in range(steps):
        patterns = sgn(np.dot(patterns, W))
    return patterns


# Recall a pattern (asynchronous)
def recallA(W, patterns, steps=5):
    n = W.shape[0]
    k = patterns.shape[0]
    sgn = np.vectorize(lambda x: -1 if x < 0 else +1)

    # Random sequence of neurons (the same neuron can be activated more than
    # one time.
    # random_seq = np.random.randint(0, n, (n,))

    random_seq = np.random.permutation(range(n))

    v = np.zeros((k, n))
    for _ in range(steps):
        for j in range(k):
            # for i in range(n):
            for i in random_seq:
                v[j, i] = sgn(np.dot(W[i], patterns[j]))
    return v


class Hopfield(object):

    def __init__(self, pattern, BINARY= False):
        self.pattern = pattern #etat d'entrée
        self.nb_neurones = len(self.pattern[0])
        self.nb_motifs = len(self.pattern)

        self.m = np.zeros((self.nb_neurones, self.nb_neurones)) #matrice des poids
        self.ratio = self.nb_motifs / self.nb_neurones

        self.nb_iterations = 0
        self.BINARY = BINARY
        self.f = lambda x: self.myfun(x, BINARY)

    def matrix(self):
        for i in self.pattern:
            z = np.array(i).reshape(1, self.nb_neurones)
            self.m += z * z.T
        self.m /= self.nb_neurones #divise et réaffecte le résultat dans m

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
    def myfun(self,x,binary=False):
        """
        fonction de seuillage
        si > theta : 1
        si < theta : min
        sinon theta
        """
        if binary :
            _min,_theta = 0,.5
        else:
            _min,_theta = -1,0
        if x > _theta : return 1
        if x == _theta : return _theta
        return _min

    def evoluer(self, datas):
    # 6. asynchrone (1 pas, maj des cells dans l'ordre)
        for i in datas:
            size = len(i)
            y = np.array(_, float)
            print("data", y)
            for j in range(size):
                o = self.asyn(self.m, y, j)
                y[j] = o
                print(i[j], '->', o)
            print("final", y, end=' ')
            if np.all(np.array(i, float) == y):
                print("stable")
            else:
                print("non stable")
        print("fin asynchrone")
        print("=" * 20)


    def stable(self, motif, etatA, etatB): #etatA = motif-1 / etatB=motif / motif = motif voulu
        if (motif == etatB) or (etatA == etatB):
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

    def bruit(self):
        pass


if __name__ == "__main__":
    pattern = [[0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]]


    h = Hopfield(pattern)
    h.matrix()
    print(h.m)
    #tester l'evolution a un pas sur le 1er pattern
    h.pas()















