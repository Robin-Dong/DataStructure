def quicksort(alist,start,end):
    n = len(alist) -1
    pivot = alist[start]
    low = start
    high = end
    if start >= high:
        return alist
    while low < high:
        while low < high and alist[high] > pivot:
            high -=1
        alist[low] = alist[high]

        while low < high and alist[low] <= pivot:
            low +=1
        alist[high] = alist[low]

    alist[low] = pivot

    quicksort(alist, start, low-1)
    quicksort(alist, low+1, end)

alist = [54,26,93,17,77,31,44,55,20,11,67]
quicksort(alist,0,len(alist)-1)
print(alist)