'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
'''
Approach
first sort the array first, with python sort

Let k is the index of first element of each set result,
loop through k -> len(nums) - 2 (duo to triplet)

then use 2 pointers technique in sorted array, to find next 2 element that make up triplet 
i = k + 1
j = len() - 1
    total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total  > 0:
                    j -= 1
                else:
                    if [nums[k],nums[i],nums[j]] not in result:
                        result.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1

k += 1

O(N^2) x M


'''

def threeSum(self, nums: list[int]) -> list[list[int]]:
    result = []

    if len(nums) < 4 and sum(nums) != 0:
        return result
    
    elif len(nums) < 4 and sum(nums) == 0:
        result.append(nums)
        return result
    
    nums.sort()
    print(nums)

    k = 0
    while k < len(nums) - 2:
        i = k + 1
        j = len(nums) - 1

        while i < j:
            total = nums[k] + nums[i] + nums[j]
            if total < 0:
                i += 1
            elif total  > 0:
                j -= 1
            else:
                if [nums[k],nums[i],nums[j]] not in result:
                    result.append([nums[k],nums[i],nums[j]])
                i += 1
                j -= 1

        k += 1
    
    return result

def threeSum_ON2(self, nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()  # O(n log n)
    
    for k in range(len(nums) - 2):
        # If the current starting number is greater than 0, 
        # it's impossible to sum up to 0 with subsequent positive numbers.
        if nums[k] > 0:
            break
            
        # Skip duplicate values for the first element
        if k > 0 and nums[k] == nums[k - 1]:
            continue
            
        i = k + 1
        j = len(nums) - 1

        while i < j:
            total = nums[k] + nums[i] + nums[j]
            
            if total < 0:
                i += 1
            elif total > 0:
                j -= 1
            else:
                result.append([nums[k], nums[i], nums[j]])
                
                # Move pointers forward
                i += 1
                j -= 1
                
                # Skip duplicate values for the second element
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                # Skip duplicate values for the third element
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
                    
    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(None, nums))

nums = [-2,0,1,1,2]
print(threeSum(None, nums))
