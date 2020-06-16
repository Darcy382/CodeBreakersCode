# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        old_right = root.right
        root.right = root.left
        root.left = old_right

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root


