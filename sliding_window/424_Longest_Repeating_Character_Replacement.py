'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''
'''
Approach
Dynamic Slicing window -> longest repeating characters -> substing
Hash Map to track char count -> repeating character

1 . Init:
    l = 0
    r = 0
    res = 0
    hashMap for char frequency count on the current window
    max_char_count_in_window = 0, max frequency so far

2. Move the right pointer r across the string:
    Update the frequency of s[r].
    Update max_char_count_in_window with the highest frequency seen so far.

3. If the tracked condition is violated (window size - maxf > k):
    Shrink the window from the left and adjust counts.

4. Else Update the result with the current window size, which are bigger

5. Return res at the end
'''
def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    res = 0
    hashMap = {}
    max_char_count_in_window = 0

    for r in range(len(s)):
        hashMap[s[r]] = hashMap.get(s[r], 0) + 1
        max_char_count_in_window = max(max_char_count_in_window, hashMap[s[r]])

        window_size = (r - l) + 1
        if window_size - max_char_count_in_window <= k:
            res = max(res, window_size)
        else:
            hashMap[s[l]] -= 1  # Decrement BEFORE moving l
            l += 1

    return res

s = "AAABABB"
k = 1
res = characterReplacement(None, s, k)
print(s)    
print(res)    

s = "AABABBA"
k = 1
res = characterReplacement(None, s, k)
print(s)    
print(res)    

s = "AB"
k = 2
res = characterReplacement(None, s, k)
print(s)    
print(res)    


s = "ABAB"
k = 2
res = characterReplacement(None, s, k)
print(s)    
print(res)    

s = "ABAA"
k = 0
res = characterReplacement(None, s, k)
print(s)    
print(res)    
