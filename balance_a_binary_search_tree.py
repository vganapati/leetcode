from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createTree(self, treeList: List) -> Optional[TreeNode]:
        if len(treeList) == 0:
            return None
        root = TreeNode(treeList.pop(0))
        nodes = [root]
        while len(treeList) > 0:
            newNodes = []
            for node in nodes:
                
                left_val = treeList.pop(0)
                if len(treeList) > 0:
                    right_val = treeList.pop(0)
                else:
                    right_val = None

                if left_val is not None:
                    node.left = TreeNode(left_val)
                    newNodes.append(node.left)
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    newNodes.append(node.right)

            nodes = newNodes
        return root
    
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # make an ordered list
        sorted_list = []
        def build_sorted_list(root):
            if root.left:
                build_sorted_list(root.left)
            sorted_list.append(root.val)
            if root.right:
                build_sorted_list(root.right)
        
        
        # build tree
        def build_tree(sorted_list):
            if len(sorted_list) == 0:
                return None
            elif len(sorted_list) == 1:
                return TreeNode(sorted_list[0])
            mid = len(sorted_list)//2
            root = TreeNode(sorted_list[mid], build_tree(sorted_list[0:mid]), build_tree(sorted_list[mid+1:]))
            return root
        
        build_sorted_list(root)
        return build_tree(sorted_list)

solution = Solution()
root = solution.createTree([1,None,2,None,3,None,4])
solution.balanceBST(root)
