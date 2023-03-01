print("------------- creation of set -----------")
a_set = set([1,2,4,6,7,8,8,9,5,2])
set1 = {1,2,4,6,3,5,3,1,3}
print("using set() -> " ,a_set)
print("using {} -> ", set1)
print('\n')

print("---------- adding an element in set ----------")
a_set.add(4)
a_set.add(10)
print("after adding element -> ", a_set)
print("\n")

print("----------------- update() --------------------")
a_set.update({11,12,14})
print("after updating elements -> ", a_set)
print("\n")

print("---------------- remove elements -------------")
print("before poping -> ", a_set)
a_set.pop() #removes 1
print("after poping -> ", a_set)
a_set.remove(12)
print("using remove() -> ",a_set)
# a_set.remove(15) throw keyError ass 15 doesn't exist
a_set.discard(2)
print("using discard() -> ", a_set)
a_set.discard(15) #doesn't throw keyError
print("using discard() -> ",a_set)
# a_set.clear()  removes all elements from set
print("\n")


print("------------ typecasting using set() ------------")
list = [1,2,6,4,3,3]
set_list = set(list)
str = "geeksforgeeks"
set_str = set(str)
dict = {1:"one", 2:"two", 3:"three"}
set_dict = set(dict)
print("list after typecasting -> ", set_list)
print('string after typecasting -> ', set_str)
print("dictionary after typecasting -> ",set_dict)
print("\n")

print("------------------ copy() -----------")
new_set = a_set.copy()
print("new set after copy -> ", new_set)
new_set.add(16)
print("after adding element -> ", new_set)
print("initial set -> ", a_set)
set2 = new_set
print("another set copy using = -> ", set2)
set2.update({17,18})
print("after updating -> ", set2)
print("initial set -> ", new_set)
print("\n")

print("---------------- union(), difference(), intersection() -----------")
union_set = a_set.union(set1)
print("Set1 ->", a_set)
print("Set2 ->", set1)
print("union of 2 sets -> ", union_set)
diff_set = a_set.difference(set1)
diff_set1 = set1.difference(a_set)
print("difference of 2 sets -> ",diff_set )
print("difference of 2 sets -> ", diff_set1)
intersection_set = a_set.intersection(set1)
print("intersection of sets -> ", intersection_set)
print('isdisjoint() -> ', a_set.isdisjoint(set1))
print("issubset() -> ", a_set.issubset(set1))
print("issuperset() -> ", a_set.issuperset(set1))
print("symmetric_difference() ->", a_set.symmetric_difference(set1))
print("\n")
