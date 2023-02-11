import random

def get_sample(nbits=3, prob=None, n=1):
    '''
        nbits: number of bits to represent number
        prob: dictionary defines the finite probability for the keys defined by a specified number of bits
        n: number random samples to return
        return: a list of random samples defined in nbits
    '''
    assert isinstance(nbits, int)
    assert isinstance(n, int)
    assert nbits > 0
    assert n >= 0

    if prob is not None:
        assert isinstance(prob, dict)
        assert len(prob) != 0
        totprob = 0.0

        for k in prob:
            assert isinstance(k, str)
            assert len(k) == nbits
            assert k.isdecimal()
            assert isinstance(prob[k], float)
            assert prob[k] >= 0.0 and prob[k] <= 1.0
            totprob = totprob + prob[k]
        assert totprob == 1
    
    res = []

    if n == 0:
        return res

    if prob is not None:
        res = random.choices(list(prob.keys()), list(prob.values()), k=n)
    else:
        upbound = (1 << nbits) - 1
        seq = []

        for i in range(0,upbound + 1):
            seq.append(format(i, '0'+ str(nbits) + 'b'))
        print(seq)
        res = random.sample(seq, k=n)

    return res
