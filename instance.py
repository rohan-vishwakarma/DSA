nums = [1, 2, 3, 8]

def missing_number(lists):
    counter = 1
    res = []
    for number in lists:
        if number != counter:
            res.append(counter)
        counter +=1

    return res

c = missing_number(nums)
print(c)
