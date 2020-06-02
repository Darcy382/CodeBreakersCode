def minWindow(s: str, t: str) -> str:
    fufilled = {}
    required = {}
    shortest = (-1, float("inf"), float("inf"))

    for char in t:
        if char in required:
            required[char] += 1
        else:
            required[char] = 1

    original_letters = required.copy()

    l = r = 0
    while r < len(s):
        print(l, r)
        print(fufilled)
        print(required)
        if s[r] in original_letters:
            if s[r] in fufilled:
                fufilled[s[r]] += 1
            else:
                fufilled[s[r]] = 1

            if s[r] in required:
                if required[s[r]] > 1:
                    required[s[r]] -= 1
                else:
                    del required[s[r]]

        while l < r and len(required) == 0:
            print(l, r)
            print(l, r)
            print(fufilled)
            print(required)
            if (r - l + 1) < shortest[2]:
                shortest = (l, r, r - l + 1)

            if s[l] in fufilled:
                if fufilled[s[l]] > 1:
                    fufilled[s[l]] -= 1
                else:
                    del fufilled[s[l]]

                if s[l] in required:
                    if required[s[l]] < original_letters[s[l]]:
                        required[s[l]] += 1
                else:
                    required[s[l]] = 1
            l += 1
        r += 1
    return shortest


                  l
                        r
print(minWindow("ADOBECODEBANC","ABC"))
                 01234567890123