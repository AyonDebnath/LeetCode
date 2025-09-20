# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.numberOfGoodNodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        max = root.val
        self.dfs_traverse(max, root)
        return self.numberOfGoodNodes


    def dfs_traverse(self, max, root):
        if root is None:
            return
        if root.val >= max:
            self.numberOfGoodNodes += 1
            max = root.val
        self.dfs_traverse(max, root.left)
        self.dfs_traverse(max, root.right)

