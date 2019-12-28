
a = [18, 17, 13, 19, 15, 11, 20]
b = [0 , 1 , 2 , 3 , 4 , 5 , 6 ]

# Can do range minimum query (get index of minimum element in a range)
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
        self._update(i, el, 1, 0, self._n - 1)


    def _update(self, i, el, p, L, R):
        mid = (L + R) // 2
        #if i == mid:
        if L == R:
            self._A[i] = el
        else:
            if i <= mid:
                self._update(i, el, 2 * p, L, mid)
            else:
                self._update(i, el, 2 * p + 1, mid + 1, R)
            a = self._A[self._st[2 * p]]
            b = self._A[self._st[2 * p + 1]]
            self._st[p] = self._st[2 * p] if self._A[self._st[2 * p]] <= self._A[self._st[2 * p + 1]] else self._st[2 * p + 1]

    # Change A[i, j+1] to common value (el)
    # not tested 
    def rangeUpdate(self, el, i, j):
        self._rangeUpdate(1, el, i, j, 0, self._n - 1)

    def _rangeUpdate(self, p, el, i, j, L, R):
        mid = (L + R) // 2
        if i == j:
            self._A[i] = el
        elif L <= i and j <= mid:
            self.__rangeUpdate(2 * p, el, i, j, L, mid)
            self._st[p] = self._st[p] if self._A[self._st[p]] <= el else i
        elif mid + 1 <= i and j <= R:
            self.__rangeUpdate(2 * p + 1, el, i, j, mid + 1, R)
            self._st[p] = self._st[p] if self._A[self._st[p]] <= el else i
        elif i <= mid and mid + 1 <= j:
            self.__rangeUpdate(2 * p, el, i, mid, L, mid)
            self.__rangeUpdate(2 * p + 1, el, mid + 1, j, mid + 1, R)
            self._st[p] = self._st[p] if self._A[self._st[p]] <= el else i
        else:
            print("this case shouldn't occur?")
            
# Can do range sum query
class SegmentTree: 

    def __init__(self, A):
        self._A = A
        self._n = len(A)
        self._st = [0] * (4 * self._n)
        self._build(1, 0, self._n - 1)

    def _build(self, p, L, R):
        if L == R:
            self._st[p] = self._A[L]
        else:
            mid = (L + R) // 2
            self._build(2 * p, L, mid)
            self._build(2 * p + 1, mid + 1, R)

            self._st[p] = self._st[2 * p] + self._st[2 * p + 1]

    def _rsq(self, p, L, R, i, j):
        if R < L:
            print("hello")
        mid = (L + R) // 2
        if L == i and R == j:
            return self._st[p]
        elif L <= i and j <= mid:
            return self._rsq(2 * p, L, mid, i, j)
        elif mid + 1 <= i and j <= R:
            return self._rsq(2 * p + 1, mid + 1, R, i, j)
        else:
            return self._rsq(2 * p, L, mid, i, j) + self._rsq(2 * p + 1, mid + 1, R, i, j)


    def rsq(self, i, j):
        return self._rsq(1, 0, self._n - 1, i, j)


    def update(self, el, i):
        self._A[i] = el
        self._update(i, el, 1, 0, self._n - 1)


    def _update(self, i, el, p, L, R):
        mid = (L + R) // 2
        if L == R:
            self._st[p] = el
        else:
            if i <= mid:
                self._update(i, el, 2 * p, L, mid)
            else:
                self._update(i, el, 2 * p + 1, mid + 1, R)
            self._st[p] = self._st[2 * p] + self._st[2 * p + 1]
