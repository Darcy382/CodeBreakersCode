# second attempt, O(M + N) time, O(1) space
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
        i
m
    5 6 7 5 6 7
    1 2 3
        n

    """
    m -= 1
    n -= 1
    i = len(nums1) - 1

    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:  # nums[m] < nums[n]
            nums1[i] = nums2[n]
            n -= 1
        i -= 1

    while n >= 0:
        nums1[i] = nums2[n]
        i -= 1
        n -= 1
    return nums1

