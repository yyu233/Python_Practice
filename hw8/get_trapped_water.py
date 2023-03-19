def get_trapped_water(seq):
    '''
        Compute units of water trapped between walls

        seq: list of wall heights in integer
        return: units of water trapped in integer
    '''
    assert isinstance(seq, list)

    for h in seq:
        assert isinstance(h, int)
        assert h >= 0

    res = 0
    size = len(seq)
    maxLeft = size * [0]
    maxRight = size * [0]

    for i in range(1, size):
        maxLeft[i] = max(maxLeft[i - 1], seq[i - 1])

    for i in range(size - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], seq[i + 1])

    for i in range(1, size - 1):
        minHeight = min(maxLeft[i], maxRight[i])
        if minHeight > seq[i]:
            res = res + (minHeight - seq[i])

    return res
