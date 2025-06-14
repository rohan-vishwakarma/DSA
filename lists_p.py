list = [11,3,5,664,6]

def smallest(list):
    try:
        if len(list) == 0:
            return ValueError("List Cannot Be Empty")

        element = list[0]
        for i in range(len(list)):
            if list[i] < element:
                element = list[i]
        return  element
    except Exception as e:
        return e

def biggest(list):
    try:
        if len(list) == 0:
            return ValueError("List Cannot Be Empty")

        element = list[0]
        for i in range(len(list)):
            if list[i] > element:
                element = list[i]
        return  element
    except Exception as e:
        return e

p = smallest(list)
p1 = biggest(list)
print("Smallest Element From The List Is = ",p)
print("Biggest Element From The List Is = ",p1)


