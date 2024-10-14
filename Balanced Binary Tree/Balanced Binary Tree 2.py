# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeightAndBalanced(self, root):
        if root is None:
            return [0, True]

        left, right = self.getHeightAndBalanced(root.left), self.getHeightAndBalanced(root.right)
        balanced = abs(left[0] - right[0]) <= 1

        return [(1 + max(left[0], right[0])), (left[1] and right[1] and balanced)]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeightAndBalanced(root)[1]