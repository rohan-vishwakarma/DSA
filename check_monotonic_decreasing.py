def monotonic(arr):
    res = True

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                res = False
    return res


p = monotonic([1, 2, 4,5])
print(p)