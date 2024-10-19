# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root, subtree):
        if root is None or subtree is None:
            return root is None and subtree is None

        if root.val != subtree.val :
            return False
        return self.isSameTree(root.left, subtree.left) and self.isSameTree(root.right, subtree.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)