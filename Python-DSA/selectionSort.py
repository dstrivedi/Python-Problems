# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)

# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when the memory write is a costly operation. 


class Solution: 
    def select(self, arr, i):
        # code here
        min_idx = i
        for j in range(i, len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        return min_idx        
    
    def selectionSort(self,arr:list,n:int)->list:
        for i in range(len(arr)):
            min_idx = self.select(arr, i)
            # swapping using temp var
            # temp = arr[min_idx]
            # arr[min_idx] = arr[i]
            # arr[i] = temp
            # swapping using slicing
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr


s = Solution()
# print(s.selectionSort([64, 34, 25, 12, 22, 11, 90],7))
# print(s.selectionSort([5, 4, 8, 2, 9, 7, 3],7))

print(s.selectionSort(["paper", "true" ,  "soap", "floppy", "flower"],5))
print(s.selectionSort(["GeeksforGeeks", "Practice.GeeksforGeeks", "GeeksQuiz"],3))

# print(selectionSort([64, 34, 25, 12, 22, 11, 90]))
# print(selectionSort([5, 4, 8, 2, 9, 7, 3]))

# print("-"*10)
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# print(bubble_sort([5, 4, 8, 2, 9, 7, 3]))