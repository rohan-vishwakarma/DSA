def mydecorate(function):
    def wrapper(*args, **kwargs):
        print("hi i am a decorator")
        return function(*args, **kwargs)
    return wrapper

@mydecorate
def hello(person):
    print(f"hello {person}")

hello("rohan")