# factorial of 5

# 5 * 4 *3 *2 * 1




class Factorial:
    def factorial(n):

        if n == 1 or n == 1:
            return 1
        number = n
        for i in range(1,n):
            number = number * (n-i)

        return number

    


