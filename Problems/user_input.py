user_input = input("Enter three numbers to calculate sum : ")

split_input = user_input.split(",")
list = []

for i in split_input:
    list.append(int(i))
    
a,b,c = list;
result = a + b -c

print(result)

