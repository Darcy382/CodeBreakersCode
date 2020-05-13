
# First attempt, O(n) time and space
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return None
        stack = []
        for item in tokens:
            try:
                item = int(item)
                stack.append(item)
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                if item == "+":
                    stack.append(num2 + num1)
                elif item == "-":
                    stack.append(num2 - num1)
                elif item == "*":
                    stack.append(num2 * num1)
                else:
                    if num2 // num2 > 0:
                        stack.append(num2 // num1)
                    else:
                        stack.append((num2 // num1) + 1)
        return stack.pop()