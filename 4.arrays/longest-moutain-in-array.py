
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
def longestMountain2(self, A: List[int]) -> int:
    longest = 0
    base = end = 0
    while base < len(A) - 1:
        if A[end + 1] > A[end]:
            while end + 1 < len(A) and A[end + 1] > A[end]:
                end += 1
            if end + 1 < len(A) and A[end + 1] < A[end]:
                while end + 1 < len(A) and A[end + 1] < A[end]:
                    end += 1
                longest = max(longest, end - base + 1)
            else:
                # Leveled off
                end += 1
        else:
            end += 1
        base = end
    return longest
