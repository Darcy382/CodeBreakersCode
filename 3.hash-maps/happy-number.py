'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

input: 19

1. 1^2 + 9^2 = 82
2. 8^2 + 2^2 = 68
3. 6^2 + 8^2 = 100
4. 1^2 + 0^2 + 0^2 = 1

output = true

input 9

1. 9^2 = 81
2. 8^2 + 1^2 = 65
3. 36 + 25 = 61
4. 37
5. 58
6. 89
7. 145
8. 42
9. 20
10. 4
11. 16
12. 37

False
'''

# First attempts in meeting w/ ben O(N) time and space????
def isHappy(num, outputs=None):
    if outputs is None:
        outputs = set()

    num = str(num)
    new_num = 0
    for digit in num:
        new_num += (int(digit) ** 2)

    if new_num == 0:
        return False
    elif new_num == 1:
        return True
    elif new_num in outputs:
        return False

    outputs.add(new_num)

    return isHappy(new_num, outputs)


def isHappyWhile(num):
    outputs = set()
    while num != 1:
        new_num = 0
        for digit in str(num):
            new_num += (int(digit) ** 2)
        num = new_num
        if num in outputs:
            return False
        else:
            outputs.add(num)

    return True

# Second attempt, same runtime
def isHappy2(self, n: int) -> bool:
    outputs = {n}
    num = n
    while num != 1:
        num = sum([int(digit)**2 for digit in str(num)])
        if num in outputs:
            return False
        else:
            outputs.add(num)
    return True