# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return None

        if root.left is None and root.right is None and root.val == sum:
            return True

        sum -= root.val

        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)

        return left or right