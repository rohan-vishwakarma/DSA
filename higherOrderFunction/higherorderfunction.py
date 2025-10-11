str = "rohanruiyiuyiuo"

dict = {}
for i in str:
    if not dict.get(i):
        dict[i] = 0
    dict[i] = dict[i] + 1

print(dict)