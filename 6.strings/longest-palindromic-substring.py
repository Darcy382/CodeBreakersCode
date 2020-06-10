def longestPalindrome(self, s: str) -> str:
    longest = []
    for i in range(len(s)):
        # odd length
        current_pal = []
        current_pal.append(s[i])
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            current_pal.append(s[k])
            current_pal.insert(0, s[j])
            j -= 1
            k += 1
        if len(current_pal) > len(longest):
            longest = current_pal

        # Even length
        j = i
        k = i + 1
        current_pal = []
        while j >= 0 and k < len(s) and s[j] == s[k]:
            current_pal.append(s[k])
            current_pal.insert(0, s[j])
            j -= 1
            k += 1
        if len(current_pal) > len(longest):
            longest = current_pal
    return "".join(longest)


# O(N^2) time, O(1) space
def longestPalindrome2(self, s: str) -> str:
    longest = (0, 0, 0)
    i = 0
    while i < len(s):
        even = self.checkPal(s, i, i + 1)
        odd = self.checkPal(s, i - 1, i + 1)
        longest = max(longest, even, odd, key=lambda x: x[2])
        i += 1
    return s[longest[0]:longest[1] + 1]

def checkPal(self, s, l, r):
    longest = (0, 0, 0)
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return (l + 1, r - 1, r - l + 1)