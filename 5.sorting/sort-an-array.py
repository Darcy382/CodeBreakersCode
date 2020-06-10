import random

# Quick sort, O(NlogN) runtime, O(1) space
def sortArray(self, nums):
    if len(nums) <= 1:
        return nums

    # quick_sort
    self.quickSort(nums)
    return nums


def quickSort(self, nums):
    random.shuffle(nums)
    self._quickSort(nums, 0, len(nums) - 1)


def _quickSort(self, nums, lo, hi):
    if lo >= hi:
        return

    pivot = self.partition(nums, lo, hi)

    self._quickSort(nums, lo, pivot - 1)

    self._quickSort(nums, pivot + 1, hi)


def partition(self, nums, lo, hi):
    pivot = nums[lo]
    swap_index = lo + 1
    for i in range(lo + 1, hi + 1):
        if nums[i] < pivot:
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index += 1
    nums[lo], nums[swap_index - 1] = nums[swap_index - 1], nums[lo]
    return swap_index - 1

# Merge sort implementation