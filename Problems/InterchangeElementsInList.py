#Given a list, write a Python program to swap first and last element of the list.

def interchange(list):
    
    #1. using temp variable
    # first_ele = list[0];
    # list[0] = list[len(list)-1]
    # list[len(list)-1] = first_ele
    
    #2. using pop 
    
    
    #3. or in a single  line approach
    list[0],list[-1] = list[-1], list[0]
    return list

print(interchange([1,2,3]))
print(interchange([12, 35, 9, 56, 24]))