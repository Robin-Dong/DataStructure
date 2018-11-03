def bucketsort(alist):
    n = len(alist)
    max_num = max(alist)
    bucket_list = [0] * (max_num+1)
    result = []
    for num in alist:
        bucket_list[num] += 1
    for i in range(len(bucket_list)):
        if bucket_list[i] != 0:
            for j in range(bucket_list[i]):
                result.append(i)
    return result


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = bucketsort(alist)
print(sorted_alist)
