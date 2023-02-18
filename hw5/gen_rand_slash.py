import numpy as np

def gen_rand_slash(m=6,n=6,direction='back'):
    '''
        Produce a uniformly random forward or backslashed image

        m: number of rows in the image
        n: number of columns in the image
        direction: string defined back or forward direction of slash
        return: Numpy array of at least 2 non-zero pixels
    '''
    assert isinstance(m, int)
    assert m > 1
    assert isinstance(n, int)
    assert n > 1
    assert isinstance(direction, str)
    assert direction == 'back' or direction == 'forward'

    k = np.random.randint(-m + 2, n - 1)
    res = np.zeros((m, n), dtype=int)

    if k > 0:
        i = 0
        for j in range(k, n):
            res[i][j] = 1
            i = i + 1
    else:
        j = 0
        for i in range(abs(k), m):
            res[i][j] = 1
            j = j + 1

    if direction == 'back':
        res = np.fliplr(res)

    return res
