import numpy as np
from collections import defaultdict
def find_convex_cover(pvertices,clist):
    """
    Finds the optimum radius of circles such that all vertices are contained
    :param pvertices:
    :param clist:
    :return:
    """

    assert isinstance(pvertices,np.ndarray)
    assert isinstance(clist,list) 


    p = np.array(pvertices)
    c = np.array(clist)
    r = defaultdict(int)
    list1 = []
    
    x = p[:, None] - c
    y = np.apply_along_axis(np.linalg.norm, -1, x)
    mins = np.argmin(y, axis=-1)

    for i, item in enumerate(mins):
        r[item] = max(y[i, item], r[item])
        
    for i in range(len(clist)):
        list1.append(r[i])

    return list1

