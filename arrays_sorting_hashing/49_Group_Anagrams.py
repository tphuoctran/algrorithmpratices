'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
'''
Approach 1 O(m x n log n)
Use hash map dict, to stored "char" version of each words as key, and values are array of original key

Approach 2 O(m x n)
Use hash map dict
define a count = [0] * 26 to count all char for each string  count[ord(char) - ord('a')] += 1
the convert array count to tuble as key in dict due to array cannot be key in dict

    
'''
def groupAnagrams_sorted(self, strs: list[str]) -> list[list[str]]:
    dict = {}

    for str in strs:
        #sort all char in str then
        #Joins the list back into a string
        key = ''.join(sorted(str))

        if key in dict:
            dict[key].append(str)
        else:
            dict[key] = [str]

    return list(dict.values())

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dict = {}
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        if key not in dict:
            dict[key] = []
        dict[key].append(s)
    return list(dict.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams_sorted(None, strs))

print(groupAnagrams(None, strs))