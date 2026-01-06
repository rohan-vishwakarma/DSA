from functools import reduce

lst = [1,2,3,4,5,6,7,8,1,10]

multiply = list(map(lambda y: y * y, lst))
even     = list(filter(lambda y: y % 2 == 0, lst))
total    = reduce(lambda a, b : a + b, list(filter(lambda i: i %2 == 0, lst)))


lst = [1, 2, 3, 4, 5]



# need to take out all the even numbers , square each element and then sum

even_square_sum = reduce(lambda a, b : a + b, map(lambda c: c * c, filter(lambda f : f %2 == 0, lst)))
print(even_square_sum)


