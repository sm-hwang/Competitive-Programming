
class FenwickTree:

    def __init__(self, A):
        # Need to auto update self._ft 
        self._ft = [0] * len(A)

    def adjust(self, k, v):
        while k < len(self._ft):
            self._ft[k] += v
            k += (k & -k)

    def rsq(self, a, b):
        return self._rsq(b) - (0 if a == 1 else self._rsq(a - 1))

    def _rsq(self, b):
        summ = 0
        while b:
            summ += self._ft[b]
            b -= (b & -b)
        return summ 

