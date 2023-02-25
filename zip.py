# Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 

# It is used to map the similar index of multiple containers so that they can be used just using a single entity. 
# Syntax :  zip(*iterators) 

# Parameters : Python iterables or containers ( list, string etc ) 
# Return Value : Returns a single iterator object, having mapped values from all the 
# containers.

#Example : python zip two lists
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
print(set(mapped))

#Example : python zip dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
a_dict = {k:v for k, v in zip(stocks,prices)}
print(a_dict)
