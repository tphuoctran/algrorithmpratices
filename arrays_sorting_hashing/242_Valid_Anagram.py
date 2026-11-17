'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
'''
Approach:

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

if len(s) != len(t), it violate anagram rulke, then returnb false

If we combine 2 string and count all letters, all letters count much be a even number
because each letter will repeated again in the other string, to the total char in count

We use 2 dict1 = {} and dict2 = {} as a hash table to store count letter in both string
Then we loop through the dict againt to check any letter's count is odd mean it violate the anagram rule

need to check egde case where 
s='aa'
t='bb'
'''

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict1 = {}
    dict2 = {}

    for i in range(len(s)):
        if s[i] in dict1:
            dict1[s[i]] += 1
        else:
            dict1[s[i]] = 1

        if t[i] in dict2:
            dict2[t[i]] += 1
        else:
            dict2[t[i]] = 1

    for char in dict1:
        if char not in dict2:
            return False
        if dict1[char] != dict2[char]:
            return False
    return True


s = "anagram"
t = "nagaram"
print(isAnagram(None, s, t))

s = "aa"
t = "bb"
print(isAnagram(None, s, t))
