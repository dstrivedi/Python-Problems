# Given a list of dictionaries, the task is to write a python program that extracts only those dictionaries that contain a specific given key value.

# Input : test_list = [{"gfg’ : 2, "is’ : 8, "good’ : 3}, {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9}, {‘love’ : 3}], key= “gfg”
# Output : [{‘gfg’: 2, ‘is’: 8, ‘good’: 3}, {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9}] 
# Explanation : gfg is present in first two dictionaries, hence extracted.

# Input : test_list = [{‘gfg’ : 2, ‘is’ : 8, ‘good’ : 3}, {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9}, {‘love’ : 3, ‘gfgs’ : 4}], key = “good”
# Output : [{‘gfg’: 2, ‘is’: 8, ‘good’: 3}] 
# Explanation : good is present in 1st dictionary, hence extracted. 

def extract(list, key):
    new_list = [sub for sub in list for k in sub.keys() if k == key]
    # if(key in dict1):
    #     new_list.append(dict1)
    # if(key in dict2):
    #     new_list.append(dict2)
    # if(key in dict3):
    #     new_list.append(dict3)
    return new_list

print(extract([{"gfg" : 2, "is" : 8, "good" : 3},{"gfg" : 1, "for" : 10, "geeks" : 9},{"love" : 3}],key = "gfg"))
