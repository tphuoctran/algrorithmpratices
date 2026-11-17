'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
'''
Approach
sorted array
2 pointer
i = 0 
j = len(nums) - 1

initze result array same as input array with all zero
result = [0] * len(nums)
k = len(nums) - 1 pointer to store result
k is go backward from len(nums) k -= 1 until < 0

if nums[i] ** 2 > nums[j] ** 2 then result[k] = nums[i] ** 2; i += 1
if nums[i] ** 2 <= nums[j] ** 2 then result[k] = nums[j] ** 2; j -= 1
'''

def sortedSquares(self, nums: list[int]) -> list[int]:
    if len(nums) < 2:
        nums[0] = nums[0] ** 2
        return nums

    result = [0] * len(nums)

    i = 0
    j = len(nums) - 1
    k = len(nums) - 1

    while k >= 0:
        if nums[i] ** 2 > nums[j] ** 2 :
            result[k] = nums[i] ** 2
            i += 1
        else:
            result[k] = nums[j] ** 2
            j -= 1
        k -= 1

    return result

nums =  [-4,-1,0,3,10]
print(sortedSquares(None, nums))

nums2 = [-5,-3,-2,-1]
print(sortedSquares(None, nums2))
