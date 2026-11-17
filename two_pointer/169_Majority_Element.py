'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
##Two Pointer approach O(n) time complexity and O(n) space complexity

def majorityElement(self, nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    countDict = {}

    while left < len(nums) and left <= right:
        if left != right:
            countDict[nums[left]] = countDict.get(nums[left], 0) + 1
            countDict[nums[right]] = countDict.get(nums[right], 0) + 1
        else:
            countDict[nums[left]] = countDict.get(nums[left], 0) + 1

        if countDict[nums[left]] > len(nums) // 2:
            return nums[left]
        
        if countDict[nums[right]] > len(nums) // 2:
            return nums[right]

        left += 1
        right -= 1

##Boyer-Moore Majority Vote algorithm time complexity O(n) and space complexity O(1)
def majorityElement2(self, nums: list[int]) -> int:

    major=nums[0]
    count = 1

    for i in range(1, len(nums)):
        if count == 0:
            major = nums[i]
            count = 1
        elif major == nums[i]:
            count += 1
        else:
            count -= 1
    return major;


input1 = [3,2,3]
print("Input: nums = ", input1)
print("Output: ", majorityElement(0, input1))

input2 = [2,2,1,1,1,2,2]
print("Input: nums = ", input2)
print("Output: ", majorityElement(0, input2))

input1 = [3,2,3]
print("Input: nums = ", input1)
print("Output: ", majorityElement2(0, input1))

input2 = [2,2,1,1,1,2,2]
print("Input: nums = ", input2)
print("Output: ", majorityElement2(0, input2))

