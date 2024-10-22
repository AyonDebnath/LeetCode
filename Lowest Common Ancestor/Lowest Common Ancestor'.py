# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # returns (bool/p, bool/q, node/common_ancestor)
        if root is None:
            return None
        left_tuple = lowestCommonAncestor(root, p, q)

        ancestor = None
        if left_tuple.__contains__(False):
            if left_tuple.__contains__(True):
                ancestor = node