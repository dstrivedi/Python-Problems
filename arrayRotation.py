def rotation(arr, n , d):
    #1. loop approach
    for i in range(0,d):
        arr.append(arr[i])
    for i in range(0,d):
        arr.pop(i);
    
    #2. list slicing approach
    arr1 = arr[d:n] + arr[0:d]
    print(arr)
    
rotation([1,2,3,4,5,6],6,2)
rotation([3,4,2,3,6,7,9],7,3)
