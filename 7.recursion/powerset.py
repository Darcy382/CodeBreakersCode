from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    sets = []
    _subsets(nums, 0, sets)
    return sets


def _subsets(nums, idx, sets):
    if idx >= len(nums):
        return
    print("yoo")
    num = nums[idx]
    for i in range(len(sets)):
        print(sets)
        sets.append(sets[i] + [num])

    sets.append([num])
    _subsets(nums, idx + 1, sets)


subsets([1, 2, 3])


# Back tracking solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for length in range(len(nums) + 1):
            self._subsets(0, [], length, nums, ans)
        return ans

    def _subsets(self, idx, current, nums_left, nums, sets):
        if nums_left == 0:
            sets.append(current)
            return
        elif idx >= len(nums):
            return

        for i in range(idx, len(nums)):
            self._subsets(i + 1, current + [nums[i]], nums_left - 1, nums, sets)