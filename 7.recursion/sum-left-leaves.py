class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self._sumLeft(root)

    def _sumLeft(self, root, left=False):
        if root is None:
            return 0
        elif left and root.left is None and root.right is None:
            return root.val

        return self._sumLeft(root.left, True) + self._sumLeft(root.right, False)