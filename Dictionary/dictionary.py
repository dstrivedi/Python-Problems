a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print("----------- simply iterate ----------")
for key in a_dict:
    print(key, ' -> ', a_dict[key])
print('\n')
    
# iterate
print("-------- dict.keys() ---------------") 
keys = a_dict.keys()
print('only keys -> ' ,keys)
print("iterate through keys() ")
for key in a_dict.keys():
    print(key)
    print(key , " -> " , a_dict[key])
print('\n')


print("-------- dict.items() ---------------") 
dict_items = a_dict.items();
print("using items() -> ", dict_items);

# Iterate through items
print("Iterate through items() in dict")
for item in a_dict.items(): 
    print(type(item)) #type -> tuple
#can be used like this too
# for key, value in a_dict.items():
#     print(key , " - > ", value)
print('\n')

# Iterate through items
print("-------- dict.values() ---------------")
value = a_dict.values()
print("only values -> " , value)
print("Iterate through values in dict")
# Using .values(), you’ll be getting access to only the values of a_dict, without dealing with the keys.
for value in a_dict.values():
    print(value)
print('\n')

print("------------ in operator ----------")
#when you use `in` in list, it checks for the element in the list
# when you use `in` in the dict, it checks for the key in the dict
# in operator to check whether the element is in dict or not
print('pet' in a_dict) #by default checked for key in dictionary
print('pet' in a_dict.keys())
print('pet' in a_dict.values())
print('pet' in a_dict.items())
print('apple' in a_dict.values())
print('\n')

print("----------- delete a key ------------")
print("before delete pet -> ", a_dict)
del a_dict['pet']
print("after deleted pet -> ", a_dict)
print("\n")

print("-------------- dict.get() --------------")
print("get value from given key -> ", a_dict.get('pet')) #None
print("get value from given key -> " , a_dict.get('fruit'))
print("\n")


print("-"*10," change dict ","-"*10)
str_dict = {
    "a":"apple", #this will change to amaze
    "b":"ball",
    "c":"cat",
    "a":"amaze"
}
print(str_dict)
