# First attempt, O(N) runtime, O(1) space
def lemonadeChange1(self, bills) -> bool:
    fives = 0
    tens = 0
    twenties = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            tens += 1
        else:
            twenties += 1
        change = bill - 5
        while change >= 10 and tens:
            tens -= 1
            change -= 10
        while change >= 5 and fives:
            fives -= 1
            change -= 5
        if change:
            return False
    return True

# Second attempt, try to hard code the change rather than while loops