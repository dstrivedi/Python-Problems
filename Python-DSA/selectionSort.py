def selectionSort(arr:list)->list:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp
    return arr

print(selectionSort([64, 34, 25, 12, 22, 11, 90]))
print(selectionSort([5, 4, 8, 2, 9, 7, 3]))

# print("-"*10)
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# print(bubble_sort([5, 4, 8, 2, 9, 7, 3]))