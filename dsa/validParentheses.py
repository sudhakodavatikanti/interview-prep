class Solution:
    def valid_parentheses(self, s: str) -> bool:
        my_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        my_stack = []
        if s[0] in my_dict.values() or len(s) < 2:
            return False
        for char in s:
            if char in my_dict.keys():
                my_stack.append(char)
            elif char in my_dict.values() and (len(my_stack) != 0 and my_dict[my_stack[-1]] == char):
                my_stack.pop()
            else:
                return False
            
        return len(my_stack) == 0


           

        