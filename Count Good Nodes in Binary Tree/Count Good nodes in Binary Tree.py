# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.noOfGoodNodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        max = root.val
        self.traverse(max, root)
        return self.noOfGoodNodes

    def traverse(self, max: int, root):
        if root is None:
            return
        if root.val >= max:
            self.noOfGoodNodes += 1
            max = root.val

        self.traverse(max, root.left)
        self.traverse(max, root.right)
