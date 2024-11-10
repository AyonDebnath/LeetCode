# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, root, left, right):
        if root is None:
            return True

        if not (root.val > left and root.val < right):
            return False

        return self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)

