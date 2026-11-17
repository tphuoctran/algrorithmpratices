'''
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 4:
Input: height = [2,2,2]
Output: 4
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
'''
Approach:
set maxArea = 0 for initial
Opposite 2 pointer technique
i = 0 left
j = len() - 1 right

area = (j - i) * min(heights[i], heights[j]) 

if area > maxArea -> let maxArea = area,

Only move i or j if
heights[i] > heights[j] -> move j backward
heights[i] <= heights[j] -> move i forward

This due to we want to find max so move the smaller height's pointer give us a change that the next aread will bigger than current calculated aread



'''
def maxArea(self, heights: list[int]) -> int:
    maxArea = 0

    left = 0
    right = len(heights) - 1

    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        if area > maxArea:
            maxArea = area

        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return maxArea

nums = [1,7,2,5,4,7,3,6]
print(nums)
print(maxArea(None, nums))