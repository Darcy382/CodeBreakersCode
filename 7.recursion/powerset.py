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