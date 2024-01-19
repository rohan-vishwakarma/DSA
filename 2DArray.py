import numpy as np



arr = np.array( [[1,2,3],[4,5,6], [7,8,9]], dtype=int,)

def print_2dArray():
    for i in range(len(arr)):

        row = arr[i]
        for j in range(len(arr)):
            print(row[j], end=" ")
        print(" ")


print("Printing the diagonals == ", arr.diagonal(axis1=1, axis2=0))


ex = arr[np.nonzero(arr > 4)]

print(ex)


linear = np.arange(10)
print(linear)


a = np.arange(6).reshape(2,3)
print(a)