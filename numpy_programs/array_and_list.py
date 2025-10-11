import sys
import time
import numpy as np

my_list = [1, 2, 4, 8, 9, 24, 21,3,3,5,7,89,7,4,4,4,4,4,6,4,3,3,25,5,5,5,57]

lists_start_time = time.time()
sizes = [i * i for i in my_list]
lists_end_time = time.time()

print(f"Time taken for list comprehension: {lists_end_time - lists_start_time:.6f} seconds")
print(f"Lists: {sizes}")

array = np.array([1, 2, 4, 8, 9, 24, 21,3,3,5,7,89,7,4,4,4,4,4,6,4,3,3,25,5,5,5,57], 'i')

lists_start_time = time.time()
modified_array = array * array
lists_end_time = time.time()

print(f"Time taken for array modification using numpy: {lists_end_time - lists_start_time:.6f} seconds")
print(f"modified_array: {modified_array}")






# Large dataset: 1 million elements
data_size = 1000000
my_list = list(range(data_size))

# List comprehension
start = time.perf_counter()
squared_list = [x * x for x in my_list]
end = time.perf_counter()
list_time = end - start

# NumPy
arr = np.arange(data_size)
start = time.perf_counter()
squared_array = arr * arr
end = time.perf_counter()
numpy_time = end - start

print(f"List time: {list_time:.6f} seconds")
print(f"NumPy time: {numpy_time:.6f} seconds")
print(f"NumPy speedup: {list_time / numpy_time:.2f}x")


