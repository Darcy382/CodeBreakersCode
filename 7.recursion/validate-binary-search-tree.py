class Solution:
    def isValidBST(self, root: TreeNode, min_val=float("-inf"), max_val=float("inf")) -> bool:
        if root is None:
            return True
        left_valid = True
        right_valid = True
        if root.left:
            if min_val < root.left.val < root.val:
                left_valid = self.isValidBST(root.left, min_val, root.val)
            else:
                left_valid = False
        if root.right:
            if root.val < root.right.val < max_val :
                right_valid = self.isValidBST(root.right, root.val, max_val)
            else:
                right_valid = False
        return left_valid and right_valid