# Python 3.6, and beyond
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_incomes = {k:incomes[k] for k in sorted(incomes)}
print("sorted dictionary -> ", sorted_incomes)

# Sort Dictionary By Key in Python
# Input:
# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Output: 
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


def sort_dict_keys(dict):
    print("-"*10, " sorting dictionary using key ", "-"*10)
    sorted_keys = {k:dict[k] for k in sorted(dict)}
    return sorted_keys

def sort_dict_values(dict):
    print("-"*10, " sorting dictionary using values ", "-"*10)
    sorted_values = {k:v for k, v in sorted(dict.items(), key=lambda x:x[1])}
    return sorted_values

print(sort_dict_values({'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}))
    
    