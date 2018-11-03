def shellsort(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j>=gap and alist[j-gap] >alist[j]:
                alist[j-gap], alist[j] = alist[j],alist[j-gap]
                j -= gap
        gap //= 2

alist = [54,26,93,17,77,31,44,55,20]
shellsort(alist)
print(alist)