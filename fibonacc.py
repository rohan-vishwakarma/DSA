
def fibonacci(n):
    if n == 0 or n == 1:
        return "Cannot Find the fibonacci"
    first , second = 0, 1
    for i in range(n):
        temp = second
        res = first + second
        print(res, end=" => ")
        first = second
        second = res


fibonacci(12)
