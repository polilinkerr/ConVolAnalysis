def inicjator(maksima, obraz, wymiary_full):
    # cdef int i
    # cdef int L
    # cdef int index

    edge = list(maksima)
    L = len(edge)
    edge_info_poor = range(-1, -1 * (L + 1), -1)
    edge_info = []

    for index in xrange(L):
        punkt = edge[index]
        obraz[punkt[2]][punkt[1]][punkt[0]] = edge_info_poor[index]
        pierwsze_nowi = budowniczy(punkt[0], punkt[1], punkt[2], 0, 0, 0, wymiary_full)
        edge_info.append(pierwsze_nowi)

    return (obraz, edge, edge_info)


# def budowniczy(int x, int y, int z, int px, int py, int pz):
def budowniczy(x, y, z, px, py, pz, wymiary_full):
    # cdef int xi, yi, zi, wx, wy, wz
    wx = wymiary_full[1]
    wy = wymiary_full[0]
    wz = wymiary_full[2]
    nowi = []
    boki = [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0),
            (-1, 1, 1), (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1),
            (1, -1, -1), (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0), (1, 1, 1)]
    for b in boki:
        xi = x + b[0]
        yi = y + b[1]
        zi = z + b[2]
        if px == xi and py == yi and pz == zi:
            continue
        if xi >= wx - 1 or yi >= wy - 1 or zi >= wz - 1:
            continue
        nowi.append((xi, yi, zi))

    return nowi


# def rdzen(obraz, edge,edge_info, int noise_lev):
def rdzen(obraz, edge, edge_info, noise_lev, wymiary_full):
    # cdef int t
    # cdef int index
    # cdef int px
    # cdef int py
    # cdef int pz
    # cdef int x
    # cdef int y
    # cdef int z
    # cdef int pix
    # cdef int plama
    # cdef int N_rem
    # cdef int Len



    """

    :type obraz: object
    """
    for t in xrange(256, noise_lev, -1):
        print t
        N_rem = 0
        Len = len(edge)
        for index in xrange(len(edge)):
            if index >= Len - N_rem:
                break
            punkt = edge[index]
            px = punkt[0]
            py = punkt[1]
            pz = punkt[2]
            do_usuniecia = []
            sasiedzi = edge_info[index]
            for j in sasiedzi:
                x = j[0]
                y = j[1]
                z = j[2]
                pix = obraz[z][y][x]
                if pix >= t:
                    plama = obraz[pz][py][px]
                    obraz[z][y][x] = plama
                    edge.append((x, y, z))
                    edge_info.append(budowniczy(x, y, z, px, py, pz, wymiary_full))
                if pix >= t or pix == 0:
                    do_usuniecia.append(j)
            if len(sasiedzi) == len(do_usuniecia):
                edge.pop(index)
                edge_info.pop(index)
                N_rem = N_rem + 1
            else:
                for j in do_usuniecia:
                    sasiedzi.remove(j)
                    edge_info[index] = sasiedzi
    del edge
    del sasiedzi
    del edge_info

    return obraz


def tlumacz(dobre):
    # cdef int i
    # cdef int j
    # cdef int k

    gotowe = []
    for i in range(len(dobre)):
        for j in range(len(dobre[1])):
            for k in range(len(dobre[1][1])):
                if dobre[i][j][k] < 0:
                    gotowe.append(((k + 1, j + 1, i + 1), (-1) * dobre[i][j][k]))
    del dobre

    return gotowe


def tlumacz2(dobre, maksima):
    # cdef int i
    # cdef int j
    # cdef int k
    # cdef int p
    # cdef int l
    # cdef int N

    l = len(maksima)
    gotowe = []
    prawie_gotowe = [[] for p in xrange(l)]
    for i in range(len(dobre)):
        for j in range(len(dobre[1])):
            for k in range(len(dobre[1][1])):
                if dobre[i][j][k] < 0:
                    prawie_gotowe[-(dobre[i][j][k] + 1)].append(-dobre[i][j][k])
    for i in xrange(l):
        gotowe.append((maksima[i], len(prawie_gotowe[i])))
    del dobre

    return gotowe
