def countSubstrings(self, s: str) -> int:
    num_pals = 0
    for i in range(len(s)):
        num_pals += 1
        num_pals += self.check_palindrome(s, i, i + 1)
        num_pals += self.check_palindrome(s, i - 1, i + 1)
    return num_pals


def check_palindrome(self, s, left, right):
    num_pals = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        num_pals += 1
        left -= 1
        right += 1
    return num_pals