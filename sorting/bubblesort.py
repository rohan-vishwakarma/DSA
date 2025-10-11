from collections.abc import Iterable

from lists_p import smallest

array = [12, 3,20,2,1,0,54]


def bubblesort(lst):
    if len(lst) == 0:
        return "iterables must not be empty"

    if not isinstance(lst, Iterable):
        return "function only accepts iterables"

    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp

    return lst



arr1= [1, 2, 3, 4, 5]
arr2= [3, 4, 5, 6, 7]

def common_elements(l1, l2):
    large = l1
    small = l2
    common = []
    if len(l2) > len(l1):
        large = l2
        small = l1
    for i in range(0,len(large)):
        if large[i] in small:
            common.append(large[i])
    return common

c = common_elements(arr2, arr1)
print(c)



