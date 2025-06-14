
 # 1, 2, 3, 4, 5
def fibonacci(number):
    if not number:
        return None
    first  = 0
    second = 1

    for i in range(number):
        current = first + second
        print(current)
        first = second
        second = current
    return ""

print(fibonacci(10))

