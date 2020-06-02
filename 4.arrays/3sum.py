# First attempt O((N)^2logN) time, and O(N) space, timeout
def threeSum(nums):
    solution_set = set()
    for i in range(len(nums)):
        target = -nums[i]
        compliments = {}
        for j in range (i+1, len(nums)):
            if nums[j] in compliments:
                solution_set.add(tuple(sorted([nums[i], compliments[nums[j]], nums[j]])))
            else:
                compliments[target - nums[j]] = nums[j]
    return solution_set

# Try the two pointer approach next time
def threeSum1(self, nums):
    nums.sort()
    sols = set()
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        target = -1 * nums[i]
        while j < k:
            temp_sum = nums[j] + nums[k]
            if temp_sum == target:
                sols.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif temp_sum < target:
                j += 1
            else: # temp_sum > target
                k -= 1
    return sols

# Try the two sum hash table option next time