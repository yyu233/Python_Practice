class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    def __repr__(self):
        return f'Interval(\'{self._a}, {self._b})'

    def __eq__(self,other):
        return self._a == other._a and self._b == other._b

    def __lt__(self,other):
        return self._b < other._b

    def __gt__(self,other):
        return self._b > other._b

    def __ge__(self,other):
        return self._b >= other._b

    def __le__(self,other):
        return self._b <= other._b

    def __add__(self,other):
        if self.__eq__(other):
            return self
        else:
            if self._a >= other._b or other._a >= self._b:
                return [self, other]
            else:
                return Interval(min(self._a, other._a), max(self._b, other._b))
