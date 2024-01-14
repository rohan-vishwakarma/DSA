number = int(input("ENTER THE NUMBER : "))

x = lambda x, y: x*y

for i in range(1, 11):
    result = number, "*", i, "=", x(number, i)
    print(result)