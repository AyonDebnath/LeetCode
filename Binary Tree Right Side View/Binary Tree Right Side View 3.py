# Definition for a binary tree node.
from collections import deque
from unittest.mock import right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        rightside = None


        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()

                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if rightside:
                res.append(rightside.val)
                rightside = None

        return res


sol = Solution()
print(sol.rightSideView(
TreeNode(1, TreeNode( 2, TreeNode(4, TreeNode(5, None,None), None), None), TreeNode( 3, None, None))
))