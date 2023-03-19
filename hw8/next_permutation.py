def next_permutation(t:tuple)->tuple:
    '''
    Generate the next permutation in lexicographic order

    t: tuple denoting permutaion
    return: tuple denoting next permutation
    '''
    assert isinstance(t, tuple)
    assert len(t) > 0

    for e in t:
        assert isinstance(e, int)
        assert e >= 0

    visited = set(t)
    assert len(visited) == len(t)

    n = len(t)
    i = n - 2
    while i >= 0 and t[i] >= t[i + 1]:
        i = i - 1

    if i < 0:
        return tuple(sorted(t))

    j = n - 1
    while j > i and t[j] <= t[i]:
        j = j - 1

    t = list(t)
    t[i], t[j] = t[j], t[i]
    t[i + 1:] = reversed(t[i + 1:])

    return tuple(t)

#print(next_permutation((3, 2, 1, 0)))
