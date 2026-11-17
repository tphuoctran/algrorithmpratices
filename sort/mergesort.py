'''
---Merge Sort---
Best - O(n log n) 
Average - O(n log n)
Worst - O(n log n)
Space - O(n) -- weekness of merge sort is that it requires additional space for the temporary arrays used in merging

Idea is
divide and conquer algorithm
works by recursively splitting the array into two halves until each subarray contains a single element
then merging those subarrays back together in sorted order 

Need 2 functioning part, one for splitting the array and another for merging the sorted subarrays

Splitting Function (recursively) - divide
    recursively splitting the array in to halves until each subarray contains a single element
    call merge_arrays back in the end
    base case(stop condition for recursively) there are only single element in the sliptting array
    
Merging Function - conquer
    merging those subarrays back together in a new sorted order array
     Use two ponter technque i on array1 and j on array 2
    compare the elements of the two subarrays and place them in the correct order in the merged array - due to it is sort so by do this array will be sort
    continue this process until all elements from both subarrays have been merged into the final sorted array
    if array1 and/or array2 still have element after compare and add to all left elements from both to in a new sorted order array
'''

def merge_sort(array: list) -> list: ##recursively Splitting array and call merge_arrays back in the end
    #base case, the signle element
    if len(array) <= 1:
        return array

    #find middle index
    mid = len(array) // 2

    #slip array in to 2 halves
    #recursively call merge sort in 2 smaller array - divide
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    #return merged array back after 2 halves sorted
    return merge_arrays(left_half, right_half)

def merge_arrays(array1: list, array2: list) -> list:
    sortedArray = []
    i = 0
    j = 0

    ## Two pointer technque i on array1 and j on array 2
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sortedArray.append(array1[i])
            i += 1
        else:
            sortedArray.append(array2[j])
            j += 1

    # Append any remaining elements from either array
    sortedArray.extend(array1[i:])
    sortedArray.extend(array2[j:])
    return sortedArray

print("Merge Sort")
unsortArray = [2, 5, 1, 0, 8, 10, 3, 4, 7, 6, 9]
print("Before sorting: {0} (Length: {1})".format(unsortArray, len(unsortArray)))
sortedArray = merge_sort(unsortArray)
print("After sorting: {0} (Length: {1})".format(sortedArray, len(sortedArray)))