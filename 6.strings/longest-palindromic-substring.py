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

# Try to do w/ constant memoroy net time