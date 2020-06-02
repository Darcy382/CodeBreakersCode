
# O(N) time and space
def isValid(S: str) -> bool:
    stack = []
    for char in S:
        if char == "c" and stack[-2:] != ['a', 'b']:
            return False
        elif char == "c":
            stack.pop()
            stack.pop()
        else:
            stack.append(char)
    return not stack
