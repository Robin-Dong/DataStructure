def insertionsort(alist):
    n = len(alist) - 1
    for i in range(n):
        for j in range(i+1,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
    return alist

li = [54,26,93,17,77,31,44,55,20,52]
result = insertionsort(li)
print(result)