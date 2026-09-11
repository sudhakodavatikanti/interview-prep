"""Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. A string is valid if:

Open brackets are closed by the same type of bracket.
Open brackets are closed in the correct order.
Every closing bracket has a corresponding open bracket of the same type.
Write a function isValid(s: str) -> bool that returns whether the string is valid."""

class Solution:
    def isValid(self, braces: str) -> bool:
        if len(braces) % 2 != 0:
            return False

        brace_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        my_stack = []
        for char in braces:
            if char in brace_map:
                if not my_stack or my_stack[-1] != brace_map[char]:
                    return False
                my_stack.pop()
            else:
                my_stack.append(char)

        return not my_stack



solution = Solution()
braces = "(]"
print(solution.isValid(braces))
    