
# First attempt O(N) runtime and O(1) space
def longestMountain1(self, A: list) -> int:
    largest = 0
    climb = True
    dec = False
    cur_mt = 0
    for i in range(len(A)):
        if i == 0:
            cur_mt = 1
            continue
        cur = A[i]
        prev = A[i - 1]
        if climb and cur > prev:  # Keep climbing
            cur_mt += 1
        elif climb and cur < prev:
            if cur_mt > 1:  # Start decend
                climb = False
                dec = True
                cur_mt += 1
        elif dec and cur < prev:  # Keep deceding
            cur_mt += 1
        elif dec and cur >= prev:  # End of mountain
            climb = True
            dec = False
            largest = max(largest, cur_mt)
            if cur == prev:
                cur_mt = 1
            else:
                cur_mt = 2
        else:  # climb cur = prev
            cur_mt = 1
    if dec:
        largest = max(largest, cur_mt)
    if largest >= 3:
        return largest
    else:
        return 0

# Try using two while loops next time