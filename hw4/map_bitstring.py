def map_bitstring(bitstrs):
    '''
        map each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s
        otherwise, map that bitstring to 1
        bitstrs: a list of bitstrings
        return: a dictionary of the so-described key-value pairs
    '''
    assert isinstance(bitstrs, list)
    
    res = {}
    for s in bitstrs:
        assert isinstance(s, str)
        assert s.isdecimal()
        cnt0 = 0
        cnt1 = 0
        for b in s:
            assert b == '0' or b == '1'
            if b == '0':
                cnt0 = cnt0 + 1
            if b == '1':
                cnt1 = cnt1 + 1
        if cnt0 > cnt1:
            res[s] = 0
        else:
            res[s] = 1

    return res
