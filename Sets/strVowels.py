vowels_set = {'a','e','i','o','u'}

def check_vowel(str):
    set_str = set(str.lower())
    new_set = set()
    for i in set_str:
        if(i in vowels_set):
            new_set.add(i)
    if(len(new_set) == len(vowels_set)):
        return "Accepted"
    else:
        return "Not accepted"   
    
def alternate(str):
    set_str = set(str.lower())
    intersection_set = set_str.intersection(vowels_set)
    if(len(intersection_set) == len(vowels_set)):
        return "Accepted"
    return "Not accepted"
     
    
print(check_vowel("geeksforgeeks"))
print(check_vowel("ABeeIghiObhkUul"))

print(alternate("geeksforgeeks"))
print(alternate("ABeeIghiObhkUul"))
