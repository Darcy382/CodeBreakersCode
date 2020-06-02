# First attempt, O(N) runtime?, O(1) space
def removeDuplicates1(self, nums) -> int:
    length = len(nums)
    i = 0
    while i < length:
        while i+1 < length and nums[i] == nums[i+1]:
            nums.pop(i+1)
            length -= 1
        i += 1
    return length


def remove_duplicates2(arr):
    # Remove duplicates in O(N) time and O(1) space, modifying the
    # array in place without using .pop()
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        arr[i + 1] = arr[j]
        i += 1

def removeDuplicates3(self, nums: List[int]) -> int:
    i = 0
    j = 0
    while j < len(nums):
        nums[i] = nums[j]
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        i += 1
    return i









