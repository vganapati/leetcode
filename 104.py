# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    elif root.left == None:
        return maxDepth(root.right)+1
    elif root.right == None:
        return maxDepth(root.left)+1
    else:
        return max(maxDepth(root.left), maxDepth(root.right))+1
        