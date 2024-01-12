arr = [1,2,3,4,5,6]

from array import array

def rotate(array, k):
    if k > len(array):
        return f"The value of {k} is greater than array length"
    point = 0
    for i in range(k):
        temp = array[point]
        del array[point] 
        array.append(temp)
    return array

p = rotate(arr,3)
print(p)



