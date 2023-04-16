def insertionSort(arr:list,n:int) -> list:
    for i in range(1,n):
        key = arr[i]
        # print(key, arr[i])
        j = i - 1
        while(j >= 0 and arr[j] > key):
            print(key, arr[i])
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] =  key
    return arr

print(insertionSort([12, 11, 13, 5, 6 ],5))