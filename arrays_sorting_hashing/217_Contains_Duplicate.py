'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.


Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.


Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

def containsDuplicate(self, nums: list[int]) -> bool:
    if len(nums) < 2:
        return False
    
    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return True

    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print("Nums = ", nums)
print("ContainsDuplicate = ", containsDuplicate(None, nums))