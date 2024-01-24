# Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.


# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88



def sumofallitems(dictionary):
    sum = 0
    for i in dictionary:
        sum+=dictionary[i]
    return sum

ob = sumofallitems({'a': 100, 'b':200, 'c':300})
print(ob)

