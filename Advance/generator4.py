# generator using list comprehension
import sys
comprehension = [i for i in range(4)]


print(sys.getsizeof(comprehension))
for i in comprehension:
    print(i, sys.getsizeof(i))
