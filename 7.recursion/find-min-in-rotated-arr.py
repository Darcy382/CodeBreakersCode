def findMin(self, nums: List[int]) -> int:
    def binarySearch(lo, hi):
        if lo == hi:
            return nums[lo]

        mid = (lo + hi) // 2
        if nums[hi] < nums[lo]:
            if nums[hi] < nums[mid]:
                return binarySearch(mid + 1, hi)
            else:
                return binarySearch(lo + 1, mid)
        else:
            return nums[lo]

    if len(nums) == 0:
        return -1

    return binarySearch(0, len(nums) - 1)


class Solution:
    '''
          m
    4 5 6 7 0 1 2
    l
                h

    if l < h:
        return lo
    elif mid > hi:
        search (mid+1, hi)
    elif l



    '''

    def findMin(self, nums: List[int]) -> int:
        if nums:
            return self._findMin(nums, 0, len(nums) - 1)
        else:
            return None

    def _findMin(self, nums, lo, hi):
        if nums[lo] <= nums[hi]:
            return nums[lo]
        mid = (lo + hi) // 2
        if nums[hi] < nums[mid]:
            return self._findMin(nums, mid + 1, hi)
        elif nums[lo] > nums[mid]:
            return self._findMin(nums, lo + 1, mid)
