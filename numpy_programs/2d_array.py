import numpy as np

two_dim_array = np.array([[1,2, 3], [4,5,6], [7, 8, 9]], 'i')

for i in range(0, len(two_dim_array)):
    for j in range(0, len(two_dim_array[i])):
        print(two_dim_array[i][j], end="")
    print("")


print("using eye ",np.eye(3,3))