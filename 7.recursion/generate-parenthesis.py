def generateParenthesis(n: int):
    combos = []
    _generateParenthesis([], [], n, n, combos)
    return combos

def _generateParenthesis(current, stack, opening, closing, combos):
    if opening:
        new_current = current[:]
        new_stack = stack[:]
        new_current.append("(")
        new_stack.append("(")
        _generateParenthesis(new_current, new_stack, opening - 1, closing, combos)
    if closing:
        if len(stack) == 0:
            return
        stack.pop()
        new_current = current[:]
        new_stack = stack[:]
        new_current.append(")")
        _generateParenthesis(new_current, new_stack, opening, closing - 1, combos)
    if not opening and not closing:
        if len(stack) == 0:
            combos.append("".join(current))
        else:
            return