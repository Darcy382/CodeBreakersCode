from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        required = Counter(t)
        current = defaultdict(int)
        satisfied = 0
        shortest = (-1, float("inf"), float("inf"))
        N = len(required)
        l = r = 0
        while r < len(s):
            char = s[r]
            if char in required:
                current[char] += 1
                if current[char] == required[char]:
                    satisfied += 1
            while satisfied == N and l <= r:
                shortest = min(shortest, (l, r, r - l + 1), key=lambda x: x[2])
                char = s[l]
                if char in required:
                    current[char] -= 1
                    if current[char] < required[char]:
                        satisfied -= 1
                l += 1
            r += 1

        if shortest[0] == -1:
            return ""

        return s[shortest[0]:shortest[1] + 1]