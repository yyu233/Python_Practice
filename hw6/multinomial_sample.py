import random
import itertools
import math

def get_all_combs_sum_to_n(n, size):
    '''
        Get all combinations which sum up to n with replacement
        n: integer, the target number
        size: combination size
        return: list of all combinations in list 
    '''
    if size == 1:
        return [n]

    nums = list(range(1, n))
    res = [list(cmb) for cmb in itertools.combinations_with_replacement(nums, size) if sum(cmb) == n]

    return res

def get_all_unique_perms(src):
    '''
        Get all unique permutations from each combination in a list
        src: list of combinations
        return: list of permutations in list
    '''
    res = []
    for cmb in src:
        for perm in itertools.permutations(cmb, len(cmb)):
            if perm not in res:
                res.append(list(perm))

    return res

def get_multinomial_PMF(cmb, p, n):
    '''
        Get the multinomial PMF
        cmb: list of cmb in tuple
        p: list of probabilities
        n: number of trials
        return: list of PMF
    '''
    denom = 1
    for i in range(len(cmb)):
        denom = denom * math.factorial(cmb[i])

    res = math.factorial(n) / denom
    for i in range(len(cmb)):
        res = res * (p[i] ** cmb[i])

    return res

def multinomial_sample(n,p,k=1):
    '''
        Return samples from a multinomial distribution

        n:= number of trials
        p:= list of probabilities
        k:= number of desired samples
    '''
    assert isinstance(n, int)
    assert n > 0

    assert isinstance(p, list)
    assert len(p) > 0
    totp = 0
    for i in p:
        assert i > 0
        totp = totp  + i
    assert totp == 1

    assert isinstance(k, int)
    assert k > 0
    
    if len(p) == 1:
        return [[n]]* k
    res = []
    cmbs = get_all_combs_sum_to_n(n, len(p))
    perms = get_all_unique_perms(cmbs)
    pmfs = []
    for perm in perms:
        pmf = get_multinomial_PMF(perm, p, n)
        pmfs.append(pmf)

    res = random.choices(perms, pmfs, k=k)

    return res
