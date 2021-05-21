#Python implementation of Quicksort

def Partition(data, lo, hi):
    pivot = data[hi]
    temp = lo - 1
    for i in range(lo,hi): #check to see if correct
        if data[i] < pivot:
            temp += 1
            swap = data[temp]
            data[temp] = data[i]
            data[i] = swap
    swap = data[temp + 1]
    data[temp + 1] = data[hi]
    data[hi] = swap
    return temp + 1

def QuickSort(data, lo, hi):
    if lo < hi:
        pivot = Partition(data, lo, hi)
        QuickSort(data, lo, pivot - 1)
        QuickSort(data, pivot + 1, hi)
    return data
