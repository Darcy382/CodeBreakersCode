
# First attempt O(N) time, O(1) space
def numSubarrayProductLessThanK1(self, nums, k: int) -> int:
    if len(nums) == 0:
        return 0
    count = 0
    start = 0
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        while product >= k and start <= i:
            product /= nums[start]
            start += 1
        count += ((i - start) + 1)
    return count

