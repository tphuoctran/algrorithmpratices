'''
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]


Example 2:

Input: nums = [1], k = 1

Output: [1]


Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
'''
Approach
Pattern
frequent -> hash map
Top K -> heap

Build a frequency map that counts how many times each number appears.

Create an empty min-heap.

For each number in the frequency map:

    Push (frequency, number) into the heap.
    If the heap size becomes greater than k, pop once to remove the smallest frequency.

After processing all numbers, the heap contains the k most frequent elements.

Pop all elements from the heap and collect their numbers into the result list.

Return the result.
'''
import heapq

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    result = []
    
    if len(nums) == 1 and k >= 1:
        return nums

    hashmap = dict()

    for n in nums:
        if n in hashmap:
            hashmap[n] += 1
        else:
            hashmap[n] = 1
    

    heap = []

    for num in hashmap.keys():
        heapq.heappush(heap, (hashmap[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

print(nums)
print(topKFrequent(None, nums, k))