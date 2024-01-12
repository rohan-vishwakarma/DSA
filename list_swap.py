def swap(arr):


    temp = arr[-1] 
    temp2 = arr[0]
    arr[0] = temp
    arr[-1] = temp2

    return arr
n = swap([1,2,3,4,5,6,7])


def swap_using_index(arr, index1, index2):

    if index1 > len(arr) or index2 > len(arr):
        return "invalid Position"

    temp1 = arr[index1]
    temp2 = arr[index2]

    for i in range(len(arr)):
        if arr[i] == temp1:
            arr[i] = temp2
        else:
            if arr[i] == temp2:
                arr[i] = temp1
    return arr
l = swap_using_index([1,2,3,4,5,6,7], 0, 1)
print([1,2,3,4,5,6,7])
print(l)
