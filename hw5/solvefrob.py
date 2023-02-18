import numpy as np

def solvefrob(coefs, b):
    '''
        Solve the Frobenius equation
        a_1*x_1 + ... + a_n*x_n = b

        coefs: list of a_i coefficients
        b: rhs constant
        return: list of solutions in tuple
    '''
    assert isinstance(coefs, list)
    assert len(coefs) > 0
    for a in coefs:
        assert a > 0

    assert isinstance(b, int)
    assert b > 0

    res = []
    npcfs = np.array(coefs)

    for s in np.ndindex(tuple(b // npcfs + 1)):
        if np.dot(npcfs, s) == b:
            res.append(s)

    return res
