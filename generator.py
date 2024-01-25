def myfunction():
    yield 1
    yield 2
    yield 3

print(type(myfunction))



# fibonacci


def fibonacci(limit):

    a = 0
    b = 1
    
    # 0, 1, 1, 2, 3, 5

    while a < limit: 
        yield a 
        a, b = b, a + b 

x = fibonacci(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


for i in x:
    print(i)




# generator expression 
generator_exp = (i * 5 for i in range(5) if i%2==0) 
  
for i in generator_exp: 
    print(i)