# Syntax : dict.pop(key, def)

# Parameters : 

# key : The key whose key-value pair has to be returned and removed.
# def : The default value to return if specified key is not present.
# Returns : Value associated to deleted key-value pair, if key is present. 
# Default value if specified if key is not present. 
# KeyError, if key not present and default value not specified. 

print("------------ dict.pop(key,def) ----------------")
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}
print(test_dict)
print("after poping -> ", test_dict["Nikhil"]) #7
# print(test_dict[1]) #keyError
# print(test_dict[1,0]) 
print("\n")


# Syntax : dict.popitem() 
# Parameters : None 
# Returns : A tuple containing the arbitrary key-value pair from dictionary. That pair is removed from dictionary. 
print("-------------- dict.popitem() ---------------")
d = {1: '001', 2: '010', 3: '011'}
print(d.popitem())
print(d)
