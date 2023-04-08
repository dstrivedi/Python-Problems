import copy

print("------------- copy dict -------------")
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
copied_dict = a_dict.copy()
a_dict["fruit"] = "orange"
a_dict.update({'dress' : "gown"})
print("copied dict -> ", copied_dict)
print("original dict after update ->",a_dict)
print("\n")

dict = {10:[10,100],20:[20,200],30:[30,300]}
new_dict = dict.copy()
# new_dict[10] = "a" error
new_dict[10].append(1000)
print("new dict -> ", new_dict)
print("origianl dict ->", dict)
print("\n")

print("---------------- deepcopy() -----------")
deep_copy_dict = copy.deepcopy(dict)
print("new_dict using deep() -> ",deep_copy_dict)
deep_copy_dict[20].append(2000)
print("new_dict after modification -> ", deep_copy_dict)
print("original dict after modification -> ", dict)
print("\n")

print("------------ using = ---------------")
assign_dict = dict
print("new dict using = -> " , assign_dict)
assign_dict.clear()
print("new dict after clearing -> " , assign_dict)
print("original dict -> ", dict)


