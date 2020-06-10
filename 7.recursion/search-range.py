from typing import List

class Solution:
    '''
          m
    5 7 7 8 8 10
          l
            h


    '''

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        self._searchRange(nums, 0, len(nums) - 1, target, output)
        return output

    def _searchRange(self, nums, lo, hi, target, output):
        print("lo", lo, "\nhi", hi)
        if lo == hi:
            output = [lo, hi]
            return
        if lo > hi or hi > len(nums) or lo < 0:
            return

        mid = (lo + hi) // 2
        if nums[mid] < target:
            self._searchRange(nums, mid + 1, hi, target, output)
        elif nums[mid] > target:
            self._searchRange(nums, lo, mid - 1, target, output)
        else:  # nums[mid] == target
            if nums[lo] < target:
                lo = (lo + mid) // 2
            else:  # nums[lo] == target
                if (lo == 0) or (lo >= 1 and nums[lo] != nums[lo - 1]):
                    output[0] = lo
                else:
                    lo -= 1
            if nums[hi] > target:
                hi = (hi + mid) // 2
            else:  # nums[hi] == target
                if (hi == len(nums) - 1) or (hi < len(nums) - 1 and nums[hi + 1] != nums[hi]):
                    output[1] = hi
                else:
                    hi += 1
            if output[0] == -1 or output[1] == -1:
                self._searchRange(nums, lo, hi, target, output)

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))