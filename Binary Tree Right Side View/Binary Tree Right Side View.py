# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> [int]:
        q = deque()
        q.append(root)

        res = []
        while q:
            temp = []
            rightNode = None
            for node in q:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
                    rightNode = node
            if rightNode is not None:
                res.append(rightNode.val)
            q = copy.deepcopy(temp)
        return res