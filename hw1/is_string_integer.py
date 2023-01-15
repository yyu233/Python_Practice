def is_string_integer(x=None):
    '''
        x: a single string character
        returns True or False if that character represents a valid integer in base 10
    '''
    assert x is not None
    assert isinstance(x, str)
    assert len(x) == 1

    return x.isdecimal()
