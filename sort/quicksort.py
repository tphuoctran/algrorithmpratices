'''
---Quick Sort---
Best - O(n log n)
Average - O(n log n)
Worst - O(n^2) -- worst case occurs when the pivot is always the smallest or largest element, leading to unbalanced partitions, it make this unstale sort algorithm, but can be mitigated by using randomized pivot selection or choosing the median as the pivot
Space - O(log n) -- quick sort is an in-place sorting algorithm, so it requires only a small amount of additional memory

Idea is
divide and conquer algorithm
the main task is moving the pivot element to the right position

works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot
the sub-arrays are then recursively sorted


Need 2 functioning part, one for partitioning the array and another for recursively sorting the sub-arrays

Partition Function - conquer
    select a pivot element from the array
    rearrange the elements in the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it
    use 2 pointer 
        i=0, as use index to move element that smallest than pivot
        j = i, as use to traveser through all until before pivot index, 
            if smaller than pivot swap i and j
                 i+=1
        if no more element smallest pivot, swap pivot to the current index i
    return the index of the pivot after partitioning (= i at the end of partitioning)

Recursive Function - divide
    recursively call quick_sort on the sub-arrays created by partitioning
    base case(stop condition for recursively) when the sub-array has one or zero elements

'''

def partitioning(array: list, start_index: int, end_index: int):
    
    # get pivot element from end idex
    pivot = array[end_index]
    pivot_index = end_index

    i = start_index 
    j = i

    while j < pivot_index:
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    #after the loop i is the pivot_index, swap the pivot with the element at i
    array[i], array[end_index] = array[end_index], array[i]
    return i 


def quicksort_sub_array(array: list, start_index: int, end_index: int):

    # Base case: list with 0 or 1 elements.
    if (start_index >= end_index):
        return
    
    # Divide the list into two smaller sublists
    pivot_index = partitioning(array, start_index, end_index)

    # Recursively sort each sublist
    quicksort_sub_array(array, start_index, pivot_index - 1)
    quicksort_sub_array(array, pivot_index + 1, end_index)
    
def quick_sort(array: list):
    #init pivot_index as the last element index

    pivot_index = len(array) - 1
    quicksort_sub_array(array, 0, pivot_index)



print("Quick Sort")
unsortArray = [2, 5, 1, 0, 8, 10, 3, 4, 7, 6, 9, 5]
print("Before sorting: ", unsortArray)
quick_sort(unsortArray)
print("After sorting: ", unsortArray)