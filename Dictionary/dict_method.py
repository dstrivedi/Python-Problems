from turtle import up


pantry_items = ['chicken','spam','egg','breadd']

new_dict = dict.fromkeys(pantry_items)

print(new_dict)

d = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four"
}

d2 = {
    5 : "five",
    6 : "six",
    7 : "seven"
}
keys = d.keys()
print(keys)

d.update(d2)
print(d.keys())