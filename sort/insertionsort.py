'''
---Insertion Sort---
Best - O(n) nearly sorted array or sorted array small dataset and time series data that added to sorted array
Average - O(n^2)
Worst - O(n^2) reverse sorted array, need to swap every element
Space - O(1)

Idea is
the list into two chunks: a sorted portion and an unsorted portion
inserting element from unsorted list to sorted list until no more need to inserting

Start with the first element of the array assume it is sorted portion of the list i = 0
Loop through list if there are smaller value than it array[i] (as = 0), swap it
After first loop done, the i = 0 is smallest value, then go next element i = 2, repeat until i = last index of array 

Two loops,
outer loop for i with i = 0 to len(a) - 1
    inner loop for j with j = i + 1 to len(a)
        if a[j] < a[i]:
            swap a[i] with a[min_index]
    then i + = 1
'''

def selection_sort(array: list, orderby: str) -> None:
    for i in range(len(array)):
        j = i + 1
        while j < len(array) and j != i:
            if orderby == "desc":
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]
            else:
                if array[j] < array[i]:
                    array[i], array[j] = array[j], array[i]
            j+=1
        i+=1

unsortArray = [2, 5, 1, 0, 8]

print("Insertion Sort")
print("Before sorting: ", unsortArray)
selection_sort(unsortArray, 'desc')
print("After sorting: ", unsortArray)