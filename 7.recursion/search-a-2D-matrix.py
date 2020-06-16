class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def get_element(idx):
            return matrix[idx // columns][idx % columns]

        def binarySearch(lo, hi):
            if hi < lo:
                return False
            mid = (lo + hi) // 2
            if get_element(mid) == target:
                return True
            elif get_element(mid) > target:
                return binarySearch(lo, mid - 1)
            elif get_element(mid) < target:
                return binarySearch(mid + 1, hi)

        rows = len(matrix)
        columns = len(matrix[0])
        return binarySearch(0, rows * columns - 1)