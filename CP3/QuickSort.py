import random

def quickSort(Arr):
    print()

    def _qs(A, s, e):
        if e - s <= 1:
            return 

        i, pivot = s, A[e - 1]
        print(pivot)
        for j in range(s, e - 1):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[e - 1] = A[e - 1], A[i]
        print(A)

        _qs(A, s, s + (e - s) // 2)
        _qs(A, s + (e - s) // 2, e)

    _qs(Arr, 0, len(Arr))

def quickSort(Arr):
    print()

    def _qs(A, s, e):
        if s < e - 1:
            return 

        i, pivot = s, A[e - 1]
        print(pivot)
        for j in range(s, e - 1):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[e - 1] = A[e - 1], A[i]
        print(A)

        _qs(A, s, s + (e - s) // 2)
        _qs(A, s + (e - s) // 2, e)

    _qs(Arr, 0, len(Arr))

def quickSort1(Arr):

    def _qs(A, l, u):
        if l < u:
            return 

        i = l
        for j in range(l, u):
            if A[j] < A[u]:
                A[j], A[i] = A[i], A[j] 
                i += 1
        A[i], A[u] = A[u], A[i]

        _qs(A, l, i - 1)
        _qs(A, i + 1, u)

    _qs(Arr, 0, len(Arr) - 1)
    
    
def checkSorted(arr):
    t = arr
    a = t.copy()
    a.sort()
    return t == a
