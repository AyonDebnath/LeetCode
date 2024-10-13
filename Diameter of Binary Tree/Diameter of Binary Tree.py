# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        leftDepth = 1 + self.maxDepth(root.left)
        rightDepth = 1 + self.maxDepth(root.right)
        return max(leftDepth, rightDepth)


    def diameterOfBinaryTree(self, root) -> int:
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        currDiameter = leftDepth + rightDepth
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(currDiameter, leftDiameter, rightDiameter)