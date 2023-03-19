def count_paths(m, n, blocks):
    '''
        2D Grid Path Search

        # denotes a blockage
        . denotes a openning

        m: horizontol rows
        n: veritcal columns
        blocks: list of tuple denoting the locations of blockage
        return: number of paths from top left to bottom right
    '''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(blocks, list)

    for c in blocks:
        assert isinstance(c, tuple)
        assert len(c) == 2
        assert isinstance(c[0], int)
        assert isinstance(c[1], int)
        assert c[0] >= 0 and c[0] <= m - 1
        assert c[1] >= 0 and c[1] <= n -1
        assert (c[0] +  c[1]) != 0
        assert (c[0] + c[1]) != (m - 1 + n - 1)

    blocks = set(blocks)
    dp = n * [0]

    if (0, 0) not in blocks:
        dp[0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if (i, j) in blocks:
                dp[j] = 0
            else:
                if j != 0:
                    dp[j] = dp[j - 1] + dp[j]

    return dp[-1]
