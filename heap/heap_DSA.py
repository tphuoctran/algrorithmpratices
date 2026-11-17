import heapq


##MIN_HEAP

arr = [3, 1, 4, 1, 5, 9, 2]
# convert array into a heap in-place. O(n)
heapq.heapify(arr)

# push 0 to the heap. O(log n)
heapq.heappush(arr, 0)

# peek the min element = 0. O(1)
arr[0]

# pop and return the min element = 0. O(log n)
min_element = heapq.heappop(arr)

# peek the new min element = 1. O(1)
arr[0]

'''
Max Heap
By default, the heapq module creates a min-heap. To create a max-heap, we can negate the values in the list and then convert it into a heap using the heapify function.
 We also need to remember to negate the values when we push and pop elements from the heap.
'''

# negate the values in the array
negated_arr = [-x for x in arr]
# convert array into a min-heap
heapq.heapify(negated_arr) 
# push 11 to the heap by negating it
heapq.heappush(negated_arr, -11)
# peek root of heap = 11
-negated_arr[0]
# pop and return the max element = 11
max_element = -heapq.heappop(negated_arr)
# peek the new max element = 9
-negated_arr[0]

'''
Storing Tuples
The heapq module can also be used to store tuples in the heap.
By default, the heap is ordered based on the first element of the tuple. 
If the first elements are equal, the second elements are compared, and so on.
'''
arr = [(3, 1), (1, 5), (4, 2), (1, 9), (5, 3), (9, 4), (2, 6)]
heapq.heapify(arr)
# pop and return the min element = (1, 5)
min_element = heapq.heappop(arr)
# peek the new min element = (1, 9)
arr[0]
# push (1, 7) to the heap, which is smaller than (1, 9)
heapq.heappush(arr, (1, 7))
# peek the min element = (1, 7)
arr[0]