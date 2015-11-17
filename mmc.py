__author__ = 'Somebody'
import numpy as np


bipolaire = [[-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1],
        [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1],
        [1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1]]
def myfun(x,binary=True):
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

def map_fun(f, matrice):
    """ applique f sur les éléments de la matrice """
    o = matrice.flat
    return np.array(list(map(f, o))).reshape(matrice.shape)


def update(oldX, newX, binary=True):
    """ permet de recopier une entrée dans le vect de sortie """
    if binary:
        _min = 0
    else:
        _min = -1
    lng = len(oldX)
    for i in range(lng):
        if newX[i] != _min and newX[i] != 1: newX[i] = oldX[i]
    return newX


def getEnergie(matrice, data):
    """ renvoie l'energie associée """
    l, c = matrice.shape
    _res = 0
    for i in range(l):
        for j in range(c):
            _res -= matrice[i, j] * data[i] * data[j]
    _res *= .5
    return _res


def check_memory(mem, data):
    """ présence en mémoire """
    return list(data.flat) in mem.values()


def asyn(m, y, i):
    """
    * m : matrice de Hopfield
    * y : donnee à traiter
    * i : index a mettre à jour
    """
    _ = map_fun(f, np.dot(y, m[..., i]))
    return _


def test_data(m, y, atmost=5):
    """
    * m : matrice de Hopfield
    * y : donnee à traiter
    * atmost : nombre max d'itérations
    """
    memory = {}
    _ok = False
    k = 0
    while k < atmost and not _ok:  # nb iteration et pas stable
        #print("\nItération %d" % k)
        memory[k] = list(y.flat)
        print("energie %.3f" % getEnergie(m, y), end=' > ')
        out = map_fun(f, np.dot(y, m))

        out = np.array(update(y.flat, out.flat, BINARY)).reshape(y.shape)
        print("input", y, end=',')
        print("sortie", out, end=',')

        if np.all(out == y):
            print('stable', end='')
            _ok = True
        else:
            print('non stable', end='')
        y = out
        if check_memory(memory, out) and not _ok:  # déjà vu ?
            _ok = True

            if _ok: print("\narret %d cycle %d" % (k, len(memory)))
        else:
            k += 1

    return out


def int2bin(v, sz, binary=True):
    """ prend un entier et renvoie le codage bin/bip associé """
    l = bin(v)[2:]
    d = sz - len(l)
    _l = '0' * d + l
    _l = [int(_) for _ in _l]  # format numérique
    if not binary: _l = [2 * _ - 1 for _ in _l]
    return _l


def bin2int(l, binary=True):
    """ prend une liste bin/bip renvoie l'entier associé """
    if not binary:
        _l = [0 if _ == -1 else 1 for _ in l]
    else:
        _l = l
    _b = ''.join([str(_) for _ in _l])
    print(_b, end=' ')
    return int(_b, 2)


def hebbian(p, sz, binary=False):
    """ p est un np.array, sz la taille, binary/bipolar le flag """
    if not binary:
        _ = (p * p.T)
    else:
        _ = np.zeros((sz, sz), float)
        for i in range(sz):
            for j in range(sz):
                _[i, j] = abs(p[0, i] + p[0, j] - 1)
    return _


def learn(m, pat, rate=1., withDiag=False, binary=False, verbose=False):
    """
        m est la matrice courante, pat est le pattern a apprendre
        rate: facteur
        rate < 0 : oubli
    """
    assert -1 <= rate <= 1, "%s in [-1 .. 1]" % rate
    _sz = len(pat)
    _p = np.array(pat, float).reshape(1, _sz)# crée une matrice de float
    _mp = hebbian(_p, _sz, binary)
    if not withDiag:
        _mp = _mp / _sz  # pour rester dans des petites valeurs
        _mp -= _mp.diagonal() * np.eye(_sz)
    _mp *= rate

    if verbose: print(_mp)

    return (m + _mp)


def findFixPoint(m, sz, binary=True):
    """
       cherche les points fixes de m
    """
    pfix = []
    mirror = dict()
    for i in range(2 ** (sz - 1)):
        x = int2bin(i, sz, binary)
        if binary:
            y = [(_ + 1) % 2 for _ in x]
        else:
            y = [-_ for _ in x]
        j = bin2int(y, binary)
        mirror[i] = j
        mirror[j] = i  # juste pour memoire
        # calcul pour x
        inp = np.array(x, float)
        _o = map_fun(f, np.dot(inp, m))
        _o = np.array(update(x, _o.flat, binary)).reshape(inp.shape)
        if np.all(inp == _o): pfix.append(i)
        # calcul pour y
        inp = np.array(y, float)
        _o = map_fun(f, np.dot(inp, m))
        _o = np.array(update(y, _o.flat, binary)).reshape(inp.shape)
        if np.all(inp == _o): pfix.append(j)

    return pfix, mirror


if __name__ == "__main__":
    # On positionne le flag binaire/bipolaire
    BINARY = False
    # On contruit la matrice de Hopfield
    # 1. Quelles sont les données à apprendre
    # 2. Quelle est la taille des données
    #datas = build_datas(BINARY)  # True / False
    datas = bipolaire

    lng = len(datas[0])


    # 3. initialisation de la matrice
    hopf = np.zeros((lng, lng))
    for _ in datas:
        # On garde la diagonale
        print("_" * 5, _, "_" * 5)
        hopf = learn(hopf, _, 1., True, BINARY, True)
        print("_" * 5, "global", "_" * 5)
        print(hopf)


    # 4. on divise par la taille et on nullifie la diag
    hopf /= lng
    hopf -= hopf.diagonal() * np.eye(lng)
    print("=" * 5, "final", "=" * 5)
    print(hopf)
#--------------------------------------------------



    # 5. On regarde si les patterns sont stables
    f = lambda x: myfun(x, BINARY)
    # presentation à un pas
    for _ in datas:
        y = np.array(_, float)
        out = test_data(hopf, y, 7)
        if np.all(y == out):
            diag = "stable"
        else:
            diag = "non stable"
        print("\ndebut", np.array(_), "->", out, diag)
        print("> next data")

    print("fin controle")
    print("*" * 20)

    # 6. asynchrone (1 pas, maj des cells dans l'ordre)

    for _ in datas:
        sz = len(_)
        y = np.array(_, float)
        print("data", y)
        for i in range(sz):
            o = asyn(hopf, y, i)
            if not BINARY and o not in (-1, 1):
                pass
            elif BINARY and o not in (0, 1):
                pass
            else:
                y[i] = o
            print(_[i], '->', o)
        print("final", y, end=' ')
        if np.all(np.array(_, float) == y):
            print("stable")
        else:
            print("non stable")
    print("fin asynchrone")
    print("=" * 20)
