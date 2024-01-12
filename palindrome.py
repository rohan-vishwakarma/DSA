
name = 'malayalam'

def check_palindrome(name):
    
    left = 0
    right = -1
    count = 0
    while left < len(name)//2:
        if name[left] != name[right]:
            return "not a palindrome"
        left +=1
        right -=1
    return True




p = check_palindrome(name)
print(p)

