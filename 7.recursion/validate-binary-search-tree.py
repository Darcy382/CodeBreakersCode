# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root)

    def _isValidBST(self, root, min_val=float("-inf"), max_val=float("inf")):
        if root is None:
            return True

        if min_val < root.val < max_val:
            return self._isValidBST(root.left, min_val, root.val) and self._isValidBST(root.right, root.val, max_val)
        else:
            return False