class Solution:
    '''
    tar = 8
     0 1 2 3 4 5
               m
    [5,7,7,8,8,10]
             l
                h

    2 2
    l h
    m

    '''

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self._searchRange(nums, 0, len(nums) - 1, target, "left"),
                self._searchRange(nums, 0, len(nums) - 1, target, "right")]

    def _searchRange(self, nums, lo, hi, target, edge):
        if hi < lo:
            return -1
        if lo == hi:
            if nums[lo] == target:
                return lo
            else:
                return -1
        mid = (lo + hi) // 2
        if edge == "right":
            mid += 1
        if nums[mid] == target:
            if edge == "left":
                return self._searchRange(nums, lo, mid, target, edge)
            else:
                return self._searchRange(nums, mid, hi, target, edge)
        elif nums[mid] < target:
            return self._searchRange(nums, mid + 1, hi, target, edge)
        else:  # nums[mid] > target
            return self._searchRange(nums, lo, mid - 1, target, edge)