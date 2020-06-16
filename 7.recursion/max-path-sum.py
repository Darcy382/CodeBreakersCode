# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        total_max = float("-inf")

        def _maxPathSum(root):
            if root is None:
                return 0

            left = _maxPathSum(root.left)
            right = _maxPathSum(root.right)

            this_max = root.val

            this_max += max(left, 0)
            this_max += max(right, 0)

            nonlocal total_max
            total_max = max(total_max, this_max)

            return root.val + max(left, right, 0)

        _maxPathSum(root)
        return total_max