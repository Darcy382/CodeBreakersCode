class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lo, hi, position):
            if hi < lo:
                return -1
            elif hi == lo:
                if nums[lo] == target:
                    return lo
                else:
                    return -1

            mid = (lo + hi) // 2
            if position == "right":
                mid += 1

            if nums[mid] < target:
                return search(mid + 1, hi, position)
            elif nums[mid] > target:
                return search(lo, mid - 1, position)
            else:
                if position == "left":
                    return search(lo, mid, position)
                else:
                    return search(mid, hi, position)

        return [search(0, len(nums) - 1, "left"), search(0, len(nums) - 1, "right")]