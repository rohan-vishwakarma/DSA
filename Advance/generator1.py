import sys


def generator_function(arr):
    for x in range(len(arr)):
        yield arr[x]


pr = generator_function([12, 3, 4, 5, 4])
print(sys.getsizeof(pr))
for i in pr:
    print(i)
