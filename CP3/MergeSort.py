import random

def merge1(A, B): 
    M, a, b = [], 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            M.append(A[a])
            a += 1
        else:
            M.append(B[b])
            b += 1

    c, C = (a, A) if a < len(A) else (b, B)
    while c < len(C):
        M.append(C[c])
        c += 1

    # if a < len(A):
    #    M.extend(A[a:])
    # if b < len(B):
    #    M.extend(B[b:])

    return M


def merge2(A, B):
    M, a, b, i = [0] * (len(A) + len(B)), 0, 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            M[i], a = A[a], a + 1
        else:
            M[i], b = B[b], b + 1
        i += 1

    c, C = (a, A) if a < len(A) else (b, B)
    while c < len(C):
        M[i] = C[c] 
        c, i = c + 1, i + 1

    return M

def mergeSort(A):
    if len(A) > 1:
        A1, A2 = A[:len(A) // 2], A[len(A) // 2:]  
        A1 = mergeSort(A1)
        A2 = mergeSort(A2)
        return merge2(A1, A2)
    return A


def merge_inplace(A, a, b): 
    pass


def mergeSort_inplace(A):
    pass
    
def checkSorted(arr):
    t = arr
    a = t.copy()
    a.sort()
    return t == a
