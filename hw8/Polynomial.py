class Polynomial:
    '''
    >>> p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
    >>> q=Polynomial({0:8,1:2,2:8,4:4})
    >>> repr(p)
     8 + 2 x + 4 x^(3)
    >>> p*3 # integer multiply
     24 + 6 x + 12 x^(3)
    >>> 3*p # multiplication is commutative!
     24 + 6 x + 12 x^(3)
    >>> p+q # add two polynomials
    16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
    >>> p*4 + 5 - 3*p - 1 # compose operations and add/subtract constants
     12 + 2 x + 4 x^(3)
    >>> type(p-p) # zero requires special handling but is still a Polynomial
     Polynomial
    >>> p*q # polynomial by polynomial multiplication works as usual
     64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
    >>> p.subs(10) # substitute in integers and evaluate
     4028
    >>> (p-p) == 0
     True
    >>> p == q
     False
    >>> p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
    >>> repr(p)
    '8 + 4 x^(3)'
    >>> p = Polynomial({2:1,0:-1})
    >>> q = Polynomial({1:1,0:-1})
    >>> p/q
     1 + x
    >>> p  / Polynomial({1:1,0:-3}) # raises NotImplementedError
    '''

    def __init__(self, param:dict):
        assert isinstance(param, dict)

        for k, v in param.items():
            assert isinstance(k, int)
            assert k >= 0
            assert isinstance(v, int)

        self.param = {}
        for k, v in param.items():
            if param[k] != 0:
                self.param[k] = v

        self.sortedKeys = sorted(self.param)

    def __repr__(self):
        res = ""
        if len(self.param) == 0:
            return "0"

        paramLen = len(self.param)
        sortedKeys = self.sortedKeys

        for i, k in enumerate(sortedKeys):
            v = self.param[k]
            if v == 0:
                continue
            if k == 0:
                if v < 0:
                    res = res + "- " + str(abs(v))
                else:
                    res = res + str(v)
            else:
                term = ""
                if k == 1:
                    if i == 0 and v < 0:
                        if abs(v) == 1:
                            term = '- x'
                        else:
                            term = f'- {abs(v)} x'
                    else:
                        if abs(v) == 1:
                            term = 'x'
                        else:
                            term = f'{abs(v)} x'
                else:
                    if i == 0 and v < 0:
                        if abs(v) == 1:
                            term = f'- x^({k})'
                        else:
                            term = f'- {abs(v)} x^({k})'
                    else:
                        if abs(v) == 1:
                            term = f'x^({k})'
                        else:
                            term = f'{abs(v)} x^({k})'
                res = res + term

            if i != paramLen - 1:
                nextKey = sortedKeys[i + 1]
                nextVal = self.param[nextKey]
                if nextVal > 0:
                    res = res + " + "
                if nextVal < 0:
                    res = res + " - "
        return res

    def __mul__(self, other):
        resParam = {}

        if isinstance(other, int):
            if other == 0:
                return Polynomial(resParam)
            else:
                for k in self.param:
                    resParam[k] = self.param[k] * other
        elif isinstance(other, Polynomial):
            selfSortedKeys = self.sortedKeys
            otherSortedKeys = other.sortedKeys

            m = len(selfSortedKeys)
            n = len(otherSortedKeys)

            for i in range(m):
                for j in range(n):
                    selfKey = selfSortedKeys[i]
                    otherKey = otherSortedKeys[j]
                    selfVal = self.param[selfKey]
                    otherVal = other.param[otherKey]

                    resKey = selfKey + otherKey
                    resVal = otherVal * selfVal

                    if resKey in resParam:
                        resVal = resVal + resParam[resKey]

                    resParam[resKey] = resVal
        else:
            raise TypeError(f'Invalid op type: {type(other)}')

        return Polynomial(resParam)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        resParam = {}

        if isinstance(other, int):
            if len(self.sortedKeys) == 0:
                resParam[0] = other
            else:
                for k, v in self.param.items():
                    resParam[k] = v
                if self.sortedKeys[0] == 0:
                    sumVal = self.param[0] + other
                    if sumVal != 0:
                        resParam[0] = sumVal
                    else:
                        del resParam[0]
                else:
                    if other != 0:
                        resParam[0] = other
        elif isinstance(other, Polynomial):
            selfSortedKeys = self.sortedKeys
            otherSortedKeys = other.sortedKeys

            i, j  = 0, 0
            m = len(selfSortedKeys)
            n = len(otherSortedKeys)

            while i != m and j != n:
                selfKey = selfSortedKeys[i]
                otherKey = otherSortedKeys[j]
                selfVal = self.param[selfKey]
                otherVal = other.param[otherKey]

                if selfKey == otherKey:
                    sumVal = selfVal + otherVal
                    if sumVal != 0:
                        resParam[selfKey] = sumVal
                    i = i + 1
                    j = j + 1
                elif selfKey < otherKey:
                    resParam[selfKey] = selfVal
                    i = i + 1
                else:
                    resParam[otherKey] = otherVal
                    j = j + 1

            if i == m and j != n:
                while j != n:
                    otherKey = otherSortedKeys[j]
                    otherVal = other.param[otherKey]
                    resParam[otherKey] = otherVal
                    j = j + 1

            if j == n and i != m:
                while i != m:
                    selfKey = selfSortedKeys[i]
                    selfVal = self.param[selfKey]
                    resParam[selfKey] = selfVal
                    i = i + 1
        else:
            raise TypeError(f'Invalid op type: {type(other)}')

        return Polynomial(resParam)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        negOther = None
        if isinstance(other, int):
            negOther = - other
        elif isinstance(other, Polynomial):
            negParam = {}
            for k, v in other.param.items():
                negParam[k] = - v
            negOther = Polynomial(negParam)
        else:
            raise TypeError(f'Invalid op type: {type(other)}')

        return self.__add__(negOther)

    def __rsub__(self, other):
        return other.__sub__(self)

    def __neg__(self):
        resParam = {}

        for k, v in self.param.items():
            resParam[k] = - v

        return Polynomial(resParam)

    def subs(self, sub):
        assert isinstance(sub, int)

        res = 0
        for k, v in self.param.items():
            res = res + v * (sub ** k)

        return res

    def __eq__(self, other):
        if isinstance(other, int):
            return len(self.param) == 0 and other == 0
        elif isinstance(other, Polynomial):
            return self.param == other.param
        else:
            raise TypeError(f'Invalid op type: {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            def degree(poly):
                while poly and poly[-1] == 0:
                    poly.pop()
                return len(poly) - 1

            N = []
            D = []
            q = {}
            nLen = self.sortedKeys[-1] + 1
            dLen = other.sortedKeys[-1] + 1

            for k in range(nLen):
                if k not in self.param:
                    N.append(0)
                else:
                    N.append(self.param[k])

            for k in range(dLen):
                if k not in other.param:
                    D.append(0)
                else:
                    D.append(other.param[k])

            degreeN = self.sortedKeys[-1]
            degreeD = other.sortedKeys[-1]

            if degreeN >= degreeD:
                while degreeN >= degreeD:
                    if N[-1] % D[-1] != 0:
                        raise NotImplementedError
                    mult = q[degreeN - degreeD] = N[-1] // D[-1]
                    multD = [cf * mult for cf in D]
                    for i in range(len(N) - 1, -1, -1):
                        j = i - (len(N) - len(multD))
                        if  j >= 0:
                            N[i] = N[i] - multD[j]
                    degreeN = degree(N)
                r = N
                if len(r) != 0:
                    raise NotImplementedError
            else:
               raise NotImplementedError

            return Polynomial(q)
        elif isinstance(other, int):
            resParam = {}

            for k, v in self.param.items():
                if v % other == 0:
                    resParam[k] = v // other
                else:
                    raise NotImplementedError

            return Polynomial(resParam)
        else:
            raise NotImplementedError
#
#if __name__ == "__main__":
#    p = Polynomial({0:8, 1:2, 3:4})
#    q = Polynomial({0:8, 1:2, 2:8, 4:4})
#    print(p)
#    print(q)
#    print("hi")
#    print(repr(p))
#    print(p * 3)
#    print(p * -3)
#    print(p * 0)
#    print(-3 * p)
#    print(p + q)
#    print(p + 3)
#    print(p + -8)
#    print(p + -9)
#    print(3 + p)
#    print(p - 3)
#    print(p - q)
#    print(q - p)
#    print(p - p)
#    print(p*4 + 5 - 3*p -1)
#    print(type(p - p))
#    print(p * q)
#    print(-p * q)
#    print(p.subs(10))
#    print((p - p) == 0)
#    print(p == q)
#    print(p == p)
#    print(1 == p)
#    n = Polynomial({2:1, 0:-1})
#    d = Polynomial({1:1, 0:-1})
#    print(n / 1)
#    print(n / d)
#    print(p / 2)
