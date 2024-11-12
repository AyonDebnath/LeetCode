# Definition for a binary tree node.
from socket import send_fds
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.lst = []

    def populate(self, root):
        if root.left is None:
            self.lst.append(root)
            self.populate(root.right)
        self.populate(root.left)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.populate(root)
        return self.lst[k-1].val