'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
##time complexity O(n) and space complexity O(n)
def twoSum(self, nums: list[int], target: int) -> list[int]:
    hashTable = {}

    for i, e in enumerate(nums):
        desired_value = target - e # value that we need to find in the hashTable, and need to meet target number
        if desired_value in hashTable:
            return [hashTable[desired_value][0], i]
        hashTable[e] = [i]



print("Two Sum")
nums1 = [2,7,11,15]
print("Input: nums = ", nums1, "target = 9")
print("Output: ", twoSum(0, nums1, 9))
nums2 = [3,2,4]
print("Input: nums = ", nums2, "target = 6")
print("Output: ", twoSum(0, nums2, 6))
nums3 = [3,3]
print("Input: nums = ", nums3, "target = 6")
print("Output: ", twoSum(0, nums3, 6))