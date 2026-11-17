'''
---Selection Sort---
Best - O(n^2)
Average - O(n^2)
Worst - O(n^2)
Space - O(1)

Start with the first element of the array as the minimum value (min_index) but for desc, we will find the max value instead of min value
Two loops,
outer loop for i with i = 0 to len(a) - 1
    inner loop for j with j = i + 1 to len(a)
    if a[j] < a[min_index]:
        min_index = j
    swap a[i] with a[min_index]
'''

def selection_sort(array :list, orderby: str) -> None:
    for i in range(len(array)):
        sel_index = i
        j = i + 1
        while j < len(array):
            if orderby == "desc": ## desc: sel_index = index of max value
                if array[j] > array[sel_index]:
                    sel_index = j
            else:
                if array[j] < array[sel_index]: ## asc: sel_index = index of min value
                    sel_index = j
            j +=1
        array[i], array[sel_index] = array[sel_index], array[i]


unsortArray = [2, 5, 1, 0, 8]

print("Selection Sort")
print("Before sorting: ", unsortArray)
selection_sort(unsortArray, 'desc')
print("After sorting: ", unsortArray)