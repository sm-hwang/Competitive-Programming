
# a = [18, 17, 13, 19, 15, 11, 20]
# b = [0 , 1 , 2 , 3 , 4 , 5 , 6 ]

# Currently for RMQ
class SegmentTree: 

    def __init__(self, A):
        self._A = A
        self._n = len(A)
        self._st = [0] * (4 * self._n)
        self._build(1, 0, self._n - 1)

    def _build(self, p, L, R):
        if L == R:
            self._st[p] = L
        else:
            mid = (L + R) // 2
            self._build(2 * p, L, mid)
            self._build(2 * p + 1, mid + 1, R)

            # Combine the two subtrees 
            # in this case for Range Minimum Query 
            p1, p2 = self._st[2 * p], self._st[2 * p + 1]
            self._st[p] = p1 if self._A[p1] <= self._A[p2] else p2

    def _rmq(self, p, L, R, i, j):
        mid = (L + R) // 2
        if L == i and R == j:
            return self._st[p]
        elif L <= i and j <= mid:
            return self._rmq(2 * p, L, mid, i, j)
        elif mid + 1 <= i and j <= R:
            return self._rmq(2 * p + 1, mid + 1, R, i, j)
        else:
            a = self._rmq(2 * p, L, mid, i, mid)
            b = self._rmq(2 * p + 1, mid + 1, R, mid + 1, j)
            return a if self._A[a] <= self._A[b] else b


    def rmq(self, i, j):
        return self._rmq(1, 0, self._n - 1, i, j)

    def update(self, el, i):
        pass

