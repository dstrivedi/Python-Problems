# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
 

# Examples:  

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

# using slicing
def swap(arr:list, pos1 :int, pos2:int) -> list:
    arr[pos1-1], arr[pos2-1] = arr[pos2-1] , arr[pos1-1]
    return arr

# using prop
def swap_with_pop(arr:list, pos1 :int, pos2:int) -> list:
    pop_item1 = arr.pop(pos1-1)
    pop_item2 = arr.pop(pos2-2)
    arr.insert(pos1-1,pop_item2)
    arr.insert( pos2-1,pop_item1)
    return arr

# using temp var
def swap_with_temp(arr:list, pos1 :int, pos2:int) -> list:
    temp = arr[pos1-1]
    arr[pos1-1] = arr[pos2-1]
    arr[pos2-1] = temp
    return arr

print(swap([23,65,19,90],1,3))
print(swap([1,2,3,4,5],2,5))

print("-"*10)
print(swap_with_pop([23,65,19,90],1,3))
print(swap_with_pop([1,2,3,4,5],2,5))

print("-"*10)
print(swap_with_temp([23,65,19,90],1,3))
print(swap_with_temp([1,2,3,4,5],2,5))
    