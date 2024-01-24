#Python | Filter the negative values from given dictionary


ini_dict = {'a':1, 'b':-2, 'c':-3, 'd':7, 'e':0}


result = filter(lambda x: x[1] >= 0.0, ini_dict.items())

print(dict(result))