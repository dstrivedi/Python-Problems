# Unzipping means converting the zipped values back to the individual self as they were. 
# This is done with the help of “*” operator.

#Example : python zip two lists
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
# converting values to print as list
mapped = list(mapped)
print("zipped result -> ",mapped)

# unzipping values
name, roll_no = zip(*mapped)
print("unzipped result : \n")
print("Name -> ", name)
print("Roll no -> ", roll_no)