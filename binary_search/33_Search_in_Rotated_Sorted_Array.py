'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

'''
'''
Approach
2 ways:
1 Run 1 binary search as below:

run 2 time binary search, first fine smallest number, 

then do binary search again
     if target > smallest numer, search on smallest -> right, other wise target < smallest number, search from left to smallest

stop condition of binary search is nums[mid] == target
'''
def search(self, nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        #base case stop condition
        if nums[mid] == target:
            return mid
        
        #Binary Search Step    
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]: ##due to rotated, target < nums[left], mean target is into rotated right
                left = mid + 1 # tagrget on the right side of mid
            else:
                right = mid - 1 # tagrget on the left side of mid
        else:
            if target < nums[mid] or target > nums[right]: ##due to rotated, target > nums[right], mean target is into rotated left
                right = mid - 1 # tagrget on t he left side of mid
            else:
                left = mid + 1 # tagrget on t he left side of mid
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(f"nums = {nums}")
print(f"target = {target}")
result = search(None, nums, target)
print(f"result = {result}")


nums = [4,5,6,7,0,1,2]
target = 3
print(f"nums = {nums}")
print(f"target = {target}")
result = search(None, nums, target)
print(f"result = {result}")