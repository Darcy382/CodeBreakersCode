
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
                    division = num2 / num1
                    if num2 % num1 == 0:
                        stack.append(int(division))
                    else:
                        stack.append(int(division))
        return stack.pop()

    #Attempt two, same runtime
    def evalRPN2(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return None

        # Create a stack
        stack = []

        for item in tokens:
            # If the item is a number, push it to the stack
            try:
                item = int(item)
                stack.append(item)
            # Otherwise, the item must be an operator, pop two items from the stack,
            # and use the operator on them.  Finally, push the result
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
                    stack.append(int(num2 / num1))
        return stack.pop()