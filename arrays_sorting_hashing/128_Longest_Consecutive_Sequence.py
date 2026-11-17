'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 
Exadictle 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Exadictle 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Exadictle 3:
Input: nums = [1,0,1,2]
Output: 3
 
Constraints:

0 <= nums.length <= 105
-10^9 <= nums[i] <= 10^9
'''
'''
Aprroach
Sorting then find sequence O(nlogn)
Hash Map O(n)
'''
def longestConsecutive(self, nums: list[int]) -> int:
    #O(nLogn) Time
    if len(nums) < 1:
        return 0
    
    if len(nums) == 1:
            return 1

    nums.sort()
    print(nums)

    result = 0
    currentSeqLen = 1
    for i in range(len(nums) - 1):
        if nums[i] - nums[i + 1] ==  - 1:
            currentSeqLen += 1
        elif nums[i] - nums[i + 1] <  - 1:
            result = max(result, currentSeqLen)
            currentSeqLen = 1
            
    result = max(result, currentSeqLen)

    return result

def longestConsecutive_2(self, nums: list[int]) -> int:
    #O(n) Time

    # Initialize a standard dictionary
    dict = {}
    res = 0
    
    for num in nums:
        # Use 'in' to handle duplicates and skip numbers already processed
        if num not in dict:
            # Safely look up neighbors; defaults to 0 if they don't exist
            left_streak = dict.get(num - 1, 0)
            right_streak = dict.get(num + 1, 0)
            
            # Calculate total combined length
            current_streak = left_streak + right_streak + 1
            
            # Register the current number and update its outer boundaries
            dict[num] = current_streak
            dict[num - left_streak] = current_streak
            dict[num + right_streak] = current_streak
            
            res = max(res, current_streak)
            
    return res


nums = [0,3,7,2,5,8,4,6,0,1]
print(nums)
print(longestConsecutive_2(None, nums))

nums1 = [100,4,200,1,3,2]
print(nums1)
print(longestConsecutive_2(None, nums1))

nums2 = [1,0,1,2]
print(nums2)
print(longestConsecutive_2(None, nums2))

nums3 = [1,2,6,7,8]
print(nums3)
print(longestConsecutive_2(None, nums3))
