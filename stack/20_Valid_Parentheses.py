'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def isValid(self, s: str) -> bool:
    #input string has only 1 char, return False
    if len(s) < 2:
        return False
    stack = []

    #mapping of the closing brackets to their corresponding opening brackets
    mapping = {
        ")": "(", 
        "}": "{", 
        "]": "["
    }

    for char in s:
        #if char is closing bracket, check in stack for valid opening, else char is opening bracket, push to stack
        if char in mapping:
            #if queue is empty, start wit closing, or the peek emelement instack is not match to closing bracket return flse
            if not stack or stack.pop() != mapping[char]:
                print("Stack: s = ", stack)
                return False
        else:
            stack.append(char)

    print("Stack: s = ", stack)
    # 'not stack', check stack is empty, return true
    return not stack


s = "(("
print("Input: s = ", s)
print("Output: ", isValid(None, s))