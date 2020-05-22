# First attempt O(N) runtime and space
def lengthOfLongestSubstring(self, s: str) -> int:
    max_len = 0
    letters = set()
    start = 0
    for index, letter in enumerate(s):
        if letter not in letters:
            letters.add(letter)
        else:
            while True:
                if s[start] == letter:
                    start += 1
                    break
                letters.remove(s[start])
                start += 1
        max_len = max(max_len, (index - start + 1))
    return max_len