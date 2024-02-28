list = ["apple", "bianca", "Radha"]

modified_to_dict = {}
for k, v in enumerate(list):
    p = modified_to_dict[f'{k}'] = v

print(modified_to_dict)

for i in reversed(list):
    print(i)
print("-----------------------------")
for j in sorted(list):
    print(j)

print(dir(enumerate))