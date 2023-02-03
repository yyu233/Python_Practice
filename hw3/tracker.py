import types
from time import sleep
import random
from datetime import datetime
import itertools as it
 
def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(p, limit):
    '''
        p: producer coroutine
        limit: the upper limit of the number of odd numbered seconds from producer for stopping the iteration
        yield: the number of odd numbered seconds that have been iterated over 
    '''
    assert isinstance(p, types.GeneratorType)
    assert isinstance(limit, int)
    assert limit >= 0

    i = 0

    while True:
        x = next(p)
        if x.seconds % 2 != 0:
            i = i +1
        if i > limit:
            break
        rx = (yield i)
        if rx is not None:
            limit = rx

