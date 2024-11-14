# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.lst = []

    def populate(self, root):
        if root is None:
            return
        if root.left is None:
            self.lst.append(root)
            self.populate(root.right)
        else:
            self.populate(root.left)
            self.lst.append(root)
            if root.right is not None:
                self.populate(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.populate(root)
        print(self.lst)
        return self.lst[k - 1].val