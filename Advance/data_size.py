import array as arr
import sys

array1 = arr.array('i', [1, 2, 3, 4, 5])
print(array1, "size of ", sys.getsizeof(array1))

for i in array1:
    print(i, "size", sys.getsizeof(i))



print("this size of a variable")
a = "rohan"
print(type(a), f"The size of variable {a} is ", sys.getsizeof(a))

print("--------------------------------------")

b = True
print(b)