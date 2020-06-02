
# O(N) time
# O(N) space
def multiply(self, num1: str, num2: str) -> str:
    return str(self.convert(num1) * self.convert(num2))

def convert(self, num: str) -> int:
    converter = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    int_num = 0
    counter = 0
    for dig in num[::-1]: # O(N)
        int_num += (converter[dig] * 10 ** counter)
        counter += 1
    return int_num