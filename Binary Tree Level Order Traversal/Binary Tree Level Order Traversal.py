# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.levels = []

        self.childNodes = []

    def levelOrder(self, root: []) -> [[]]:
        curr = root

        if curr is None:
            return []

        self.childNodes.append(curr)
        while self.childNodes:
            tempChildNodes = []
            for node in self.childNodes:
                if node.left:
                    tempChildNodes.append(node.left)
                if node.right:
                    tempChildNodes.append(node.right)


            temp = []
            for node in self.childNodes:
                temp.append(node.val)
            self.levels.append(temp)
            self.childNodes = tempChildNodes

        return self.levels


