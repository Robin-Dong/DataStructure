def bubblesort(alist):
    n = len(alist)-1
    for i in range(n,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    return alist

li = [54,26,93,17,77,31,44,55,20]
result = bubblesort(li)
print(result)