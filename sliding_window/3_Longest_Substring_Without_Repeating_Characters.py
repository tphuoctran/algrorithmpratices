'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''
'''
Approach
pattern: 
    substring -> slicing window, no fixed substring lenght input -> no-fixed slicing window
    no duplicate characters -> hashmap

using slicing window with
i = 0, anchor pointer

j = len - 1, moving pointer
loop the string until end 

each char add to hashset dict to track of duplicated

if char in hashset 
Shrink the window from the left until the duplicate is removed
while s[j] in hashset:
    hashset.remove(s[i])
    i += 1 

'''

def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    hashset = set()

    longest_substring_left = 0
    longest_substring_right = 0

    i = 0
    for j in range(len(s)):

        if s[j] in hashset:
            # Shrink the window from the left until the duplicate is removed
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1

        hashset.add(s[j])
        if j - i > longest_substring_right - longest_substring_left:
            longest_substring_left, longest_substring_right = i, j

    longest_substring = s[longest_substring_left:longest_substring_right + 1]
    print(longest_substring)
    return len(longest_substring)


s3 = "dvdf"
print(s3)
print(lengthOfLongestSubstring(None, s3))

s = "abcabcdb"
print(s)
print(lengthOfLongestSubstring(None, s))

s1 = "bbbbb"
print(s1)
print(lengthOfLongestSubstring(None, s1))

s2 = "pwwkew"
print(s2)
print(lengthOfLongestSubstring(None, s2))
