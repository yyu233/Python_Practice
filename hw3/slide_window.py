def slide_window(x, width, increment):
    '''
        x: a list of values
        width: positive integer represents the window width
        increment: positive integer represents the window stride
        return: list of overlapping lists from the sliding operation
    '''
    assert isinstance(x, list)
    assert isinstance(width, int)
    assert isinstance(increment, int)
    assert width > 0 and increment > 0

    res = []
    n = len(x)
    for i in range(0, n, increment):
        m = i + width - 1
        if m < n:
            stripe = x[i: m + 1]
            res.append(stripe)

    return res
