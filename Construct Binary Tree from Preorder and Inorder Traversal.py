# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] :
            return TreeNode()

        root = preorder[0]
        mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:], in)