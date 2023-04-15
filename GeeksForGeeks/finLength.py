import copy

def finLength(n : int, color : list, radius : list) -> int:
    color_copy = copy.deepcopy(color)
    radius_copy = copy.deepcopy(radius)
    i = 0
    while(len(color) > 1 and len(color) > i):
        if((len(color) == 2 and color[0] == color[1]) and (len(radius) == 2 and radius[0] == radius[1])):
            color.clear()
            radius.clear()
        elif((color[i] == color[i+1]) and (radius[i] == radius[i+1])):
            color.remove(color_copy[i])
            color.remove(color_copy[i+1])
            
            radius.remove(radius_copy[i])
            radius.remove(radius_copy[i+1])
        # print("after removal -> " , color, radius, i)
        i += 1
    
    return len(color)

def finLength_stack(n : int, color : list, radius : list) -> int:
    stack = []
    for i in range(n):
        lst =[color[i],radius[i]]
        if stack and stack[-1]==lst:
            stack.pop()
        else:
            stack.append(lst)
    return len(stack)

def finLength_submitted(self, N : int, color :list, radius :list) -> int:
        # code here
        ans = []
        for i in range(N):
            if(len(ans) == 0):
                ans.append([color[i],radius[i]])
            elif(ans[-1][0]==color[i] and ans[-1][1] == radius[i]):
                ans.pop()
            else:
                ans.append([color[i], radius[i]])
        return len(ans)

print(finLength(3,[2,2,5],[3,3,4]))
print(finLength(4,[1,3,3,1],[2,5,5,2]))
print(finLength(15, [31 ,6, 3, 48, 84, 18, 57, 73, 4, 4, 73, 4, 4,4,4],[53, 23, 44, 61, 96, 1, 97, 15, 83, 97, 97, 97, 83, 97, 97]))
