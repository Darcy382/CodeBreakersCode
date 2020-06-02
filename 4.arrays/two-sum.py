
# First attempt, O(N) time and space
def twoSum(self, nums: List[int], target: int) -> List[int]:
    target_nums = {}
    for i, num in enumerate(nums):
        if num in target_nums:
            return [target_nums[num], i]
        else:
            target_nums[target - num] = i

# Try the two pointer approach next time
def twoSum2(nums):
    nums = list(zip(nums, range(len(nums))))
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        temp_sum = nums[i][0] + nums[j][0]
        if temp_sum == target:
            return (nums[i][1], nums[j][1])
        elif temp_sum < target:
            i += 1
        else:  # temp_sum > target:
            j -= 1
    return -1