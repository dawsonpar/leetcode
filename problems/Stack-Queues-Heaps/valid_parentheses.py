"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets. 
Open brackets must be closed in the correct order. 
Every close bracket has a corresponding open bracket of the same type.

Solution
- Use a stack
- Push open brackets to stack
- When you come to a closed bracket pop from the stack and see if they match
- Use a hashmap to match brackets types
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
