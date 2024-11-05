# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root.val, root.val, root)

    def isValid(self, min, max, root):
        if root is None:
            return True
        elif root.left and root.left.val >= min:
            return False
        elif root.right and root.right.val <= max:
            return False

        if root.val < min:
            min = root.val
        if root.val > max:
            max = root.val

        return self.isValid(min, max, root.left) and self.isValid(min, max, root.right)