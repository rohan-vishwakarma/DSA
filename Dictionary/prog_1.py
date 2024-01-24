# Python – Extract Unique values dictionary values


myDict = {
    'rohan': [5, 6, 7, 8],
    'Kavya': [10, 11, 7, 5],
    'sakshi': [6, 12, 10, 8],
    'Rohit': [1, 2, 5]
}
arr = []
for value in myDict.keys():
    print(value, '=>', myDict[value])

    for j in range(len(myDict[value])):
        arr.append(myDict[value][j])

print(list(set(arr)))


