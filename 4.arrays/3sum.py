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
