from collections import defaultdict
import copy

def rec(cMap, k, i, cmmWords):
    res = []

    if i == len(k):
        return res
    
    partLen = k[i]
    candList = cmmWords[partLen]

    for cand in candList:
        cMapCopy = copy.deepcopy(cMap)
        isValid = True
        for c in cand:
            if c not in cMapCopy:
                isValid = False
                break
            else:
                cMapCopy[c] = cMapCopy[c] - 1
                if cMapCopy[c] == 0:
                    del cMapCopy[c]
        if isValid:
            recRes = rec(cMapCopy, k, i + 1, cmmWords)
            if len(recRes) == 0:
                recRes.append(cand)
                res.append(recRes)
            else:
                for cmb in recRes:
                    cmb.append(cand)
                    res.append(cmb)

    return res

def descrambler(w, k):
    '''
        A generator outputs phrase based on a dictionary of commonly used words
        w: a string of n lower-case letters
        k: k tuple of integers, jth element of the tuple defines the partiton length of w
        yield: a list of phases
    '''
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    
    kSum = 0
    for i in range(len(k)):
        assert k[i] > 0
        kSum = kSum + k[i]

    assert kSum == len(w)

    res = []
    cmmWords = defaultdict(list)
    cMap = {}

    path = "/tmp/google-10000-english-no-swears.txt"
    #path = "./google-10000-english-no-swears.txt"
    with open(path, "r") as f:
        wordList = f.read().split("\n")
        for word in wordList:
            n = len(word)
            cmmWords[n].append(word)

    for c in w:
        if c in cMap:
            cMap[c] = cMap[c] + 1
        else:
            cMap[c] = 1
    
    recRes = rec(cMap, k, 0, cmmWords)
    for cmb in recRes:
        if len(cmb) == len(k):
            cmb.reverse()
            s = ' '.join(cmb)
            res.append(s)
    for s in res:
        yield s
