from typing import List

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
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        2 3 1 1 4
                i
        '''
        i = last_valid = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= last_valid:
                last_valid = i
            i -= 1
        return last_valid == 0