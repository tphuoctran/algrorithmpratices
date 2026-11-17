'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

'''
'''
Approach:
Binary Search

Initialize left = 0, right = n - 1, and store the first element as the current answer.

While left <= right:

    If the current window is already sorted, update the answer with nums[left] and stop.

    Compute mid.

    Update the answer with nums[mid].

    If the left half is sorted:
        Move search to the right half.

    Otherwise:
        Search in the left half.

Return the smallest value found.

'''
from typing import List

def findMin(self, nums: List[int]) -> int:
    min_num = nums[0]
    left = 0
    right = len(nums) -1

    while left <= right:

        #Stop condition
        if nums[left] <= nums[right]:
            min_num = min(min_num, nums[left])
            break

        mid = right - left // 2
        min_num = min(min_num, nums[mid])

        #Binary Search Step          
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return min_num

nums = [3,4,5,1,2]
print(findMin(None, nums))



nums = [4,5,6,7,0,1,2]
print(findMin(None, nums))