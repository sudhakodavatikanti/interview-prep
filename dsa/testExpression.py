"""You are given a list of strings representing a mathematical expression in postfix notation. In postfix notation, each operator appears after its two operands.

For example:

["4", "2", "+", "3", "*"]

represents:

(4 + 2) × 3 = 18"""


import operator

class Solution:
    def evaluate_test_expression(self, tokens: list[str]) -> int:
        my_stack = []
        action_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for current_char in tokens:
            print('Current char: ', current_char)
            if current_char in action_map or current_char == '/':
                right = my_stack.pop()
                left = my_stack.pop()

                if current_char == '/':
                    result = int(left / right)
                else:
                    result = action_map[current_char](left, right)
                print(result)
                my_stack.append(result)
            else:
                my_stack.append(int(current_char))


        return my_stack.pop()

solution = Solution()
tokens = ["4", "2", "+", "3", "*"]
print(solution.evaluate_test_expression(tokens))
       