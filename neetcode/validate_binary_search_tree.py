"""
https://neetcode.io/problems/valid-binary-search-tree
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, left_bound, right_bound):
            if node is None:
                return True
            if not(node.val < right_bound and node.val > left_bound):
                return False
            
            return (isValid(node.left, left_bound, node.val) and isValid(node.right, node.val, right_bound))
        
        return isValid(root, float("-inf"), float("inf"))