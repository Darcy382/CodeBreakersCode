def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    2 0 1
    i
    l
        g
    """
    lt = 0
    gt = len(nums) - 1
    i = 0

    while i <= gt:
        if nums[i] > 1:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        elif nums[i] < 1:
            nums[i], nums[lt] = nums[lt], nums[i]
            i += 1
            lt += 1
        else:  # nums[i] == 1
            i += 1