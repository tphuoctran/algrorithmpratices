'''
---Bubble Sort---
Best - O(n) nearly sorted array or sorted array small dataset
Average - O(n^2)
Worst - O(n^2) reverse sorted array, need to swap every element
Space - O(1)

Two pointer i , j iterate through the array (a)
Two loops, 
outer loop for i with i = 0
    j = i + 1
    inner loop for j 
If element at a[j] < element at i swap them
If sort by descending order, swap if a[j] > a[i]
'''

def bubble_sort(array :list, orderby: str) -> None:
    for i in range(len(array)):
        j = i + 1
        while j < len(array):
            if orderby == "desc":
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]
            else:
                  if array[j] < array[i]:
                    array[i], array[j] = array[j], array[i]
            j += 1

unsortArray = [2, 5, 1, 0, 8]

print("Bubble Sort")
print("Before sorting: ", unsortArray)
bubble_sort(unsortArray, 'desc')
print("After sorting: ", unsortArray)