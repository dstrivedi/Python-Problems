# Deleting/Updating from a String
# In Python, Updation or deletion of characters from a String is not allowed. This will cause an error because item assignment or item deletion from a String is not supported. Although deletion of the entire String is possible with the use of a built-in del keyword. This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned. Only new strings can be reassigned to the same name. 

str1 = "Python"
str1 = "geeks"

# str1[0] = "P" error

list1 =list(str1)
list1[0] = "G"

print("".join(list1))

str2 = "GeeksForGeeks"
str2 = str2[:5] + str2[8:]
print(str2)
del str2