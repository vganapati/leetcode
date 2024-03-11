# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if len(nums) == 1:
        return TreeNode(nums[0])
    elif len(nums) == 0:
        return None
    else:
        middle = len(nums)//2
        root = TreeNode(nums[middle])
        root.left = sortedArrayToBST(nums[:middle])
        root.right = sortedArrayToBST(nums[middle+1:])
        return root