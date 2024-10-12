# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthHelper(self, root, maxNum):
        if root is None:
            return maxNum
        maxNum1 = self.maxDepthHelper(root.left, maxNum + 1)
        maxNum2 = self.maxDepthHelper(root.right, maxNum + 1)

        return max(maxNum1, maxNum2)

    def maxDepth(self, root) -> int:
        return self.maxDepthHelper(root, 0)

