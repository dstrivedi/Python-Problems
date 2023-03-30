def interchange(list):
    list[0], list[-1] = list[-1] , list[0]
    return list
    # new_list = [list[-1:],list[1:-1:],list[0:1]]
    # return sum(new_list,[]) #flatten the list

def alternative(list):
    for i in range(len(list)-1):
        if(i == 0):
            temp = list[i] 
            list[i] = list[len(list)-1] 
            list[len(list)-1] = temp
    return list



print(interchange([1,2,3,4]))
print(interchange([3,5,2,6,8,9]))

print(alternative([1,2,3,4]))
print(alternative([3,5,2,6,8,9]))
