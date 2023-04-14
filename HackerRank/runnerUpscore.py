# Given list is [2,3,6,6,5] . 
# The maximum score is 6 , second maximum is 5. Hence, we print 5 as the runner-up score.

def runnerUpScore(arr:list,n:int)->int:
    set_arr = list(set(arr))
    # print("initial:",set_arr)
    for i in range(len(set_arr)):
        # print("outerloop : ", set_arr[i])
        for j in range(i, len(set_arr)):
            # print("Inner loop : ", set_arr[j])
            if(set_arr[i] < set_arr[j]):
                # print("under if : ")
                # print(set_arr[i], set_arr[j])
                # print("...")
                temp = set_arr[i]
                set_arr[i] = set_arr[j]
                set_arr[j] = temp
                # print(set_arr)
    print(set_arr)
    return set_arr[1]

print(runnerUpScore([2,6,6,3,5],5))
print(runnerUpScore([64, 25, 12, 22, 11], 5))