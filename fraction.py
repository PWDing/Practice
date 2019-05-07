def gcd(num_a, num_b):
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_a


class Fraction:
    def __init__(self, numerator, denominator):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise ValueError("numerator and denominator must be integer!")

        cancel_factor = gcd(numerator, denominator)
        self.num = numerator // cancel_factor
        self.den = denominator // cancel_factor

    def __repr__(self):
        return '%d/%d' % (self.num, self.den)

    def __str__(self):
        if self.num % self.den == 0:
            return str(self.num // self.den)
        return '%d/%d' % (self.num, self.den)

    def get_num(self):
        if self.num % self.den == 0:
            return self.__str__()
        return self.num

    def get_den(self):
        if self.num % self.den == 0:
            return self.__str__()
        return self.den

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.num = self.__add__(other).get_num()
        self.den = self.__add__(other).get_den()
        return Fraction(self.num, self.den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __isub__(self, other):
        self.num = self.__sub__(other).get_num()
        self.den = self.__sub__(other).get_den()
        return Fraction(self.num, self.den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __imul__(self, other):
        self.num = self.__mul__(other).get_num()
        self.den = self.__mul__(other).get_den()
        return Fraction(self.num, self.den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __itruediv__(self, other):
        self.num = self.num * other.den
        self.den = self.den * other.num
        return Fraction(self.num, self.den)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __ne__(self, other):
        return self.num * other.den != self.den * other.num

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num


a_fraction = Fraction(1, 3)
b_fraction = Fraction(1, -9)
a_fraction /= b_fraction
print(b_fraction)
