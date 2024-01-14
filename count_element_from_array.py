def array(arr):
    dict = {}
    for i in range(0, len(arr)):
        dict[arr[i]] = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                dict[arr[i]] += 1

    return dict

list = [1,2,3,4,4,6,7,0, 0, 0]
p = array(list)
print(p)