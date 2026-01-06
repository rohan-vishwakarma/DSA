from typing import List

def selection_sort(elements: List[int]) -> List[int]:
    n = len(elements)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

    return elements

l = [1, 2, 7, 44, 122, 3, 22, 6, 0]
print(selection_sort(l))
