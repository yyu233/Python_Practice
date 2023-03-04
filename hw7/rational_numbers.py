import math

class Rational:
    '''
       >>> r = Rational(3,4)
       >>> repr(r)
       '3/4'
       >>> -1/r
       -4/3
       >>> float(-1/r)
       -1.3333333333333333
       >>> int(r)
       0
       >>> int(Rational(10,3))
       3
       >>> Rational(10,3) * Rational(101,8) - Rational(11,8)
       977/24
       >>> sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)])
       [1/100, 9/8, 10/3, 10]
       >>> Rational(100,10)
       10
       >>> -Rational(12345,128191) + Rational(101,103) * 30/ 44
       166235595/290480806
    '''

    def __init__(self, a, b):
        assert isinstance(a, int)
        assert isinstance(b, int)
        
        if a < 0 and b < 0:
            a = -a
            b = -b
        elif a > 0 and b < 0:
            a = -a
            b = -b

        gcd = math.gcd(a,b)
        
        self.a = a // gcd
        self.b = b // gcd

    def __repr__(self):
        if self.a % self.b == 0:
            return str(self.a // self.b)
        else:
            return f'{self.a}/{self.b}'

    def __neg__(self):
        return Rational(-self.a, self.b)

    def __add__(self, other):
        if isinstance(other, Rational):
            denom = math.lcm(self.b, other.b)
            lnumer = self.a * (denom // self.b)
            rnumer = other.a * (denom // other.b)
            numer = lnumer + rnumer
            gcd = math.gcd(numer, denom)

            return Rational(numer // gcd, denom // gcd)
        elif isinstance(other, int):
            return Rational(self.a + other * self.b, self.b)

    def __radd__(self, other):
        if isinstance(other, int):
            return Rational(self.a + other * self.b, self.b)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other * self.b - self.a, self.b)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.a, self.b * other.b)
        elif isinstance(other, int):
            return Rational(self.a * other, self.b)
        elif isinstance(other, float):
            return float(self) * other
        else:
            raise TypeError(f'Invalid type: {type(other)}')

    def __rmul__(self, other):
        if isinstance(other, int):
            return Rational(self.a * other, self.b)
        elif isinstance(other, float):
            return other * float(self)
        else:
            raise TypeError(f'Invalid type: {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b, self.b * other.a)
        elif isinstance(other, int):
            return Rational(self.a, self.b * other)
        elif isinstance(other, float):
            return float(self) / other
        else:
            raise TypeError(f'Invalid type: {type(other)}')

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(other * self.b, self.a)
        elif isinstance(other, float):
            return other / float(self)
        else:
            raise TypeError(f'Invalid type: {type(other)}')

    def __float__(self):
        return self.a / self.b

    def __int__(self):
        return self.a // self.b

    def __eq__(self, other):
        return float(self) == float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __abs__(self):
        return Rational(abs(self.a), abs(self.b))

def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''
        Compute the square root of rational number

        x: Rational
        abs_tol: Rational, represents the absolute precision
        retuns: Rational, square root of x to the absolute precision of abs_tol
    '''
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)
    assert x >= 0
    assert abs_tol >= 0

    l = 0
    r = x

    while l <= r:
        mid = l + (r - l) / 2
        sq = mid * mid

        if abs(float(mid) - math.sqrt(float(x))) <= abs_tol:
            return mid

        if sq < x:
            l = mid
        else:
            r = mid
