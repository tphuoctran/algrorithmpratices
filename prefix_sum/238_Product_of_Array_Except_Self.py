'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input:
nums = [1, 2, 3, 4]
Output: [24,12,8,6]

Example 2:
Input:
nums = [-1, 1, 0, -3, 3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
'''
Approach

Notice that
the product of all the elements of nums except nums[i] = the product of all the elements before nums[i] * the product of all the elements after nums[i]
prefix and suffix sum technique

prefix [] = product of element before i
prefix[0] = 1
prefix[1] = prefix[0] * num[0] = 1 * 1 = 1
prefix[2] = prefix[1] * num[1] = 1 * 2 = 2
prefix[3] = prefix[2] * num[2] = 2 * 3 = 6
...
....
suffix [] = product of element after i

suffix[3] = 1
suffix[2] = suffix[3] * num[3] = 1 * 4 = 4
suffix[1] = prefix[2] * num[2] = 4 * 3 = 12
suffix[0] = prefix[1] * num[1] = 12 * 2 = 24

=> result[0] = prefix[0] *  suffix[0] = 1 * 24 = 24
=> result[1] = prefix[1] *  suffix[1] = 1 * 12 = 12
=> result[2] = prefix[2] *  suffix[2] = 2 * 4 = 8
=> result[3] = prefix[3] *  suffix[3] = 6 * 1 = 6
'''

def productExceptSelf(self, nums: list[int]) -> list[int]:

    prefix = [0] * len(nums)
    suffix = [0] * len(nums)

    prefix[0] = 1
    suffix[-1] = 1

    i = 1
    j = len(nums) - 2
    while i < len(nums):
        prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix[j] = suffix[j + 1] * nums[j + 1]
        i += 1
        j -= 1
        
    for i in range(len(nums)):
        nums[i] = prefix[i] * suffix[i]
    return nums

nums = [1, 2, 3, 4]
print(nums)
print(productExceptSelf(None, nums))

nums = [-1, 1, 0, -3, 3]
print(nums)
print(productExceptSelf(None, nums))