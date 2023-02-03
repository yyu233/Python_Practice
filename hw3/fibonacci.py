def fibonacci(n):
    '''
        fibonacci number computed by a generator
        n: non-negative integer
        return the current fibonacci number
    '''
    assert n >= 0
    a = 0
    b = 1
    
    for i in range(n):
        a,b = b, a + b
        yield a
