
def selectionsort(alist):
    n = len(alist) - 1
    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]
    return alist

li = [54,26,93,17,77,31,44,55,20]
result = selectionsort(li)
print(result)