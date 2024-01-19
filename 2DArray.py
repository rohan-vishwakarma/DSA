import numpy as np



arr = np.array( [[1,2,3],[4,5,6], [7,8,9]], dtype=int,)

for i in range(len(arr)):

    row = arr[i]
    for j in range(len(arr)):
        print(row[j], end=" ")
    print(" ")


