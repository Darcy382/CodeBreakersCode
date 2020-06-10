# # second attempt, O(M + N) time, O(1) space
# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#         i
# m
#     5 6 7 5 6 7
#     1 2 3
#         n
#
#     """
#     m -= 1
#     n -= 1
#     i = len(nums1) - 1
#
#     while m >= 0 and n >= 0:
#         if nums1[m] >= nums2[n]:
#             nums1[i] = nums1[m]
#             m -= 1
#         else:  # nums[m] < nums[n]
#             nums1[i] = nums2[n]
#             n -= 1
#         i -= 1
#
#     while n >= 0:
#         nums1[i] = nums2[n]
#         i -= 1
#         n -= 1
#     return nums1

def merge2(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
              i
        n
    1 2 3 0 0 0
    2 5 6
        m
    i
    n
    1
   m


    """
    i = m + n - 1
    m -= 1
    n -= 1
    print(m)
    while i >= 0:
        if n >= 0 and m >= 0:
            if nums1[n] >= nums2[m]:
                nums1[i] = nums1[n]
                n -= 1
            else:
                nums1[i] = nums2[m]
                m -= 1
        elif n >= 0:
            break
        elif m >= 0:  # m >= 0
            nums1[i] = nums2[m]
            m -= 1
        i -= 1
    return nums1

merge2([1], 1, [], 0)


