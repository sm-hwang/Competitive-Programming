import random

# Using end index (e) that is one larger than last element in subarray being sorted, i.e. A[s:e] is the array being 
# considered by _qs()
def quickSort(Arr):
    
    def _qs(A, s, e):
        if e - s <= 1:
            return 

        i, pivot = s, A[e - 1]
        for j in range(s, e - 1):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[e - 1] = A[e - 1], A[i]

        _qs(A, s, i)
        _qs(A, i + 1, e)

    _qs(Arr, 0, len(Arr))

# Array being considered by _qs() is A[s], ..., A[e], i.e. A[s:e + 1]
def quickSort1(Arr):
    
    def _qs(A, l, u):
        if l >= u:
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
    

# For testing

# Check if list is sorted
def checkSorted(arr):
    t = arr
    a = t.copy()
    a.sort()
    return t == a

# Test whether sorting algorithm gives correct answer to random inputs
def checkSortAlgo(sort_algo, arr_size_bound, low, up, loop_count):
    for _ in range(loop_count):
        a = [random.randint(low,up) for i in range(random.randint(0, arr_size_bound))]
        sort_algo(a)
        if not checkSorted(a):
            print(a)
