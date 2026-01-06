from functools import reduce
from optparse import make_option

from library.enumeration_program import elements

# Question: Given a list of numbers [1, 2, 3, 4], apply a function to square each number.
square = list(map(lambda x : x * x, [1, 2, 3]))
print(square)

# Question: Convert a list of strings ["hello", "world"] to uppercase.
upper = list(map(lambda x: x.upper(), ["hello", "world"]))
print(upper)

# Question: Given a list of numbers [10, 20, 30], add 5 to each number.
add = list(map(lambda a: a + 5, [10, 20, 30]))
print(add)

# Question: From the list [1, 2, 3, 4, 5, 6], keep only even numbers.
even = list(filter(lambda e: e % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(even)

# Question: From the list ["apple", "banana", "cat", "dog"], keep only strings longer than 3 characters.
three_char = list(filter(lambda x: len(x) > 3,  ["apple", "banana", "cat", "dog"]))
print(three_char)

# Question: From the list [0, -1, 2, -3, 4], keep only positive numbers.
positive = list(filter(lambda x : x > 0, [0, -1, 2, -3, 4]))
print(positive)

# Question: Given a list of numbers [1, 2, 3, 4], compute their sum
sum_of_elements = reduce(lambda a , b: a + b, [1, 2, 3, 4])
print(sum_of_elements)

# Question: From the list [2, 3, 4], compute the product of all numbers
product = reduce(lambda a, b: a * b, [2, 3, 4])
print(product)

# Question: Given a list of strings ["a", "b", "c"], concatenate them into a single string.
string = reduce(lambda a , b : a + b,  ["a", "b", "c"])
print(string)


#---------------------------------------------------- Advance ----------------------------------------------------------------

# Question: Given a list of tuples [(1, 2), (3, 4), (5, 6)], apply a function to compute the product of each tuple's elements.
product_of_each_tuple = map(lambda a: reduce(lambda r, b: r * b, a), [(1, 2), (3, 4), (5, 6)])
print(list(product_of_each_tuple))

# Question: Given a list of dictionaries [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}],
# create a new list with formatted strings like "Name: <name>, Age: <age>".
new_string = map(lambda element: f"Name: {element['name']} , Age: {element['age']}", [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}])
print(list(new_string))

# Question: Given a nested list [[1, 2], [3, 4, 5], [6]], apply a function to compute the sum of each sublist.
sum_of_sublist = map(lambda x: reduce(lambda b, a: b + a, x), [[1, 2], [3, 4, 5], [6]])
print(list(sum_of_sublist))


# Question: From a list of dictionaries [{"id": 1, "score": 85}, {"id": 2, "score": 90}, {"id": 3, "score": 75}],
# keep only dictionaries where the score is greater than 80 and the id is even.

dictionary = list(filter(lambda a : a["score"] > 80 and a["id"]% 2  ==0 , [{"id": 1, "score": 85}, {"id": 2, "score": 90}, {"id": 3, "score": 75}]))
print(dictionary)

# Question: Given a list of strings ["abc123", "def456", "ghi", "789"], keep only strings that contain both letters and digits.
letter_and_digits = list(filter(lambda y: any(i.isalpha() for i in y) and any(k.isdigit() for k in y), ["abc123", "def456", "ghi", "789"]))
print(letter_and_digits)

# Question: From a nested list [[1, 2, 3], [4, 5], [6, 7, 8, 9]], keep only sublists whose elements sum to an even number.
even_num = filter(lambda x: reduce(lambda y,z : y + z, x) % 2 == 0, [[1, 2, 3], [4, 5], [6, 7, 8, 9]])
print(list(even_num))

# Question: Given a list of lists [[1, 2], [3, 4], [5, 6]], merge all sublists into a single list by concatenating them.
merge = reduce(lambda q, w: str(q) + "" + str(w),  map(lambda a: reduce(lambda r, c : str(r) + "" + str(c), a), [[1, 2], [3, 4], [5, 6]]))
print(list(merge))
