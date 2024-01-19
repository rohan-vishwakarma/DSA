
# the *args is a non keyword argument which is used to pass variable number of arguments to a function

# The **Kwargs are the keyword argument One can think of the kwargs as being a dictionary that maps each keyword to the 
# value that we pass alongside it. 
# That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

def myfunction(cars, *args):
    for a in args:
        return cars, "=>",a

f = myfunction("Cars", "Mercedes", "BMW", "Audi", "Lexis")


def myfunction2(**kwargs):
    dict ={}
    for key, value in kwargs.items():
        dict[f"{key}"] = value
    return dict


k = myfunction2(name="rohan", Age="12", city="Thane")
print(k)