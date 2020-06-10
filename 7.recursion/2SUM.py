from typing import List

# Recursive ht solution, O(N) time and space
def twoSum(self, nums: List[int], target: int) -> List[int]:
    ht = {}
    return self._twoSum(nums, ht, 0, target)


def _twoSum(self, arr, ht, idx, target):
    if idx == len(arr):
        return -1
    num = arr[idx]
    if num in ht:
        return (ht[num], idx)
    else:
        ht[target - num] = idx
        return self._twoSum(arr, ht, idx + 1, target)