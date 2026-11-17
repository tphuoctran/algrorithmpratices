'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
'''
Approach:
0. Loop  through string remove non-alphanumeric, and covert to lower()
1. Use 2 pointer i = 0, and j = len() - 1
2. Loop until i <= j, i and j go as opposite direction wih i = i + 1, and j = j -1 
    e[i] must  = e[j], otherwise return false
'''

def isPalindrome(self, s: str) -> bool:
    cleanedStr = ""
    for char in s:
         if char.isalnum():
            cleanedStr += char.lower()

    i = 0
    j= len(cleanedStr) - 1
    while i < j:
        if cleanedStr[i] != cleanedStr[j]:
            return False
        i +=1
        j -=1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(None, s))