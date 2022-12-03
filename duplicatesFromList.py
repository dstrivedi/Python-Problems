# Program to print duplicates from a list of integers
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]


# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]

from collections import Counter
list1 = [-1, 1, -1, 8]
list2 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# Method 1: Using the Brute Force approach
def duplicates(list):
    duplicates = []
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if(list[i] == list[j]) and list[j] not in duplicates:
                duplicates.append(list[j])
    return duplicates

print(duplicates(list1))
print(duplicates(list2))

# Method 2 : USing Count() function from collection module
cnt = Counter(list2)
print("Counter: ", cnt)
