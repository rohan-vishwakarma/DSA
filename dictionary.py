dictionary = {
    "name" :"rohan",
    "age": 21,
    "city": "mumbai",
    "point" : 18
}

dictionary.update({"name": "rohan v"})
dictionary.pop("name")


for key, value in dictionary.items():
    print(f"key is {key} and value is {value}")

