from typing import List

def bubble_sort(list_of_elements: List) -> List:
    if not isinstance(list_of_elements, List):
        raise ValueError("invalid type")

    if len(list_of_elements) == 0 or len(list_of_elements) == 1:
        return list_of_elements

    for i in range(0, len(list_of_elements) - 1):
        for j in range(0, len(list_of_elements) -i - 1):
            if list_of_elements[j] > list_of_elements[j + 1]:
                temp = list_of_elements[j + 1]
                list_of_elements[j + 1] = list_of_elements[j]
                list_of_elements[j] = temp

    return list_of_elements

l = [1, 2, 7, 44, 3, 22, 6, 0]
bs = bubble_sort(l)
print(bs)