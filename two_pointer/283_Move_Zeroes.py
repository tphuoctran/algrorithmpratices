'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''
'''
Approach
2 pointer
i = 0, is anchor pointer, only move when swap or not 0
j = 1, is moving pointer

if i = 0, and j <> 0, swap i j
if i = 0, j = 0, j + 1

if i != 0, j = 0,  i + 1, j + 1
if i != 0, j != 0,  i + 1, j + 1
'''

def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2 and nums[0] == 0:
        return nums

    i = 0
    j = 1

    while j < len(nums):
        if nums[i] == 0 and nums[j] == 0:
            j += 1
        elif nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] =  nums[j], nums[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1
        


nums = [0,1,2,3,4,12]
moveZeroes(None, nums)
print(nums)