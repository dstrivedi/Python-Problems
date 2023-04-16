# Time Complexity: O(N2)
# Auxiliary Space: O(1) 

def bubble_sort(arr:list) -> list:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def bubbleSort(arr:list) -> list:
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 4, 8, 2, 9, 7, 3]))

print("-"*10)
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 4, 8, 2, 9, 7, 3]))