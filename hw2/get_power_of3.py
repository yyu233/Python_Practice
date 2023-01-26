def get_power_of3(x):
    '''
        Decompose integer by a set of weights {1,3,9,27} without reusing element
        param: x is integer from 1 to 40
        return: a 4-element list of the decomposition of x
    '''
    assert isinstance(x, int)
    assert x >=1 and x <= 40

    base3rep = []

    while x > 0:
        base3rep.append(x % 3)
        x = x // 3

    base3rep.append(0)

    for i in range(len(base3rep) - 1):
        if base3rep[i] == 2:
            base3rep[i] = -1
            base3rep[i + 1] = base3rep[i + 1] + 1

    base3rep = base3rep + [0] * (4 - len(base3rep))

    for i in range(4):
        if base3rep[i] == 3:
            if base3rep[i+1] == -1:
                base3rep[i] = 0
                base3rep[i + 1] =0
            elif base3rep[i+1] == 1:
                base3rep[i] = 0
                base3rep[i + 1] = -1
                base3rep[i + 2] = 1
            else:
                base3rep[i] = 0
                base3rep[i + 1] = 1

    return base3rep[:4]
