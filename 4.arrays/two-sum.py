
# First attempt, O(N) time and space
def twoSum(self, nums: List[int], target: int) -> List[int]:
    target_nums = {}
    for i, num in enumerate(nums):
        if num in target_nums:
            return [target_nums[num], i]
        else:
            target_nums[target - num] = i

# Try the two pointer approach next time
