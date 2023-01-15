def convert_hex_to_RGB(x=None):
    '''
        x: a list of color hex-codes (e.g., ['#FFAABB'])
        return a list of RGB-tuples (e.g., [(255, 170, 187)]
    '''
    res = []
    assert x is not None
    assert isinstance(x, list)
    for i in x: 
        assert isinstance(i, str)
        assert len(i) == 7
        res.append((int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)))

    return res
