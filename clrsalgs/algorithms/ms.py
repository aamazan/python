# Python implementation of Merge sort
import math as m

def merge(A,p,q,r)
 none = q - p + 1
 ntwo = r - q
 L = []
 R = []
 for i in range(1,none):
    L.append(A[p+i-1])
 for j in range(1,ntwo):
    R.append(A[q+j])
L.append(NULL)
R.append(NULL)
i = 1
j = 1
for k in range(p, r)
    if L[i] <= R[j]:
        A[k] = L[i]
        i+=1
    else:
        A[k] = R[j]
        j+=1


def mergesort(A,p,r)
    if p < r:
        q = m.floor(((p+r)/2))
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
