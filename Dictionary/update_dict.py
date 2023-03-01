# updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
# Syntax: dict.update([other])

# Parameters: This method takes either a dictionary or an iterable object of key/value pairs (generally tuples) as parameters.

# Returns: It doesn’t return any value but updates the Dictionary with elements from a dictionary object or an iterable object of key/value pairs.

dict = {1:"one", 2: "two", 3:"three"}
dict_1 = {1:"ONE"}
print("dict before updation -> " , dict)
dict.update(dict_1)
print("dict after updation -> ", dict)

# update the Dictionary with iterable
dict_1.update(A ="TWO", B ="THREE")
print("update with iterable -> " , dict_1 )

