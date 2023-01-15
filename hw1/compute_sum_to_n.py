def compute_sum_to_n(n):
    '''
        n: non-negative integer
        return the sum of all non-negative integers up to and including n
    '''
    assert n is not None
    assert isinstance(n, int)
    assert n >= 0

    return (n + 1) / 2 * (0 + n)
