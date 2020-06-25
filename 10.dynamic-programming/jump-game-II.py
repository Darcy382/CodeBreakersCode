class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        N = len(nums)

        dp = [float("inf")] * N

        dp[0] = 0

        max_idx = 0
        for i in range(N):
            if nums[i] + i > max_idx:
                for j in range(max_idx + 1, i + nums[i] + 1):
                    if j == len(nums):
                        break
                    dp[j] = dp[i] + 1
                max_idx = nums[i] + i
                if max_idx >= len(nums) - 1:
                    return dp[i] + 1

        return -1      