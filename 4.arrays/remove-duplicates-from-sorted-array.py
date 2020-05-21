# First attempt, O(N) runtime?, O(1) space
def removeDuplicates1(self, nums: List[int]) -> int:
    length = len(nums)
    i = 0
    while i < length:
        while i+1 < length and nums[i] == nums[i+1]:
            nums.pop(i+1)
            length -= 1
        i += 1
    return length

