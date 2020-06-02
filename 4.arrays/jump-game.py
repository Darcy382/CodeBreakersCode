# First and second attempt O(N) time and O(1) space
def canJump(self, nums) -> bool:
    max_idx = 0
    for idx, num in enumerate(nums):
        if max_idx < idx:
            return False
        else:
            max_idx = max(max_idx, idx + num)
    return True

# Third attempt, try going backwards
