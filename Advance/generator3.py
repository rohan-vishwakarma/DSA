import sys
import array as arr


def array_function(array):
    tmp_array = arr.array('i', array)
    for i in range(len(tmp_array)):
        yield tmp_array[i]


a = [1, 2, 3, 4, 6, 7]
p = array_function(a)
for i in p:
    print(i)