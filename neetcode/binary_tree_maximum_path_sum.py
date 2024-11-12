from typing import List, Optional

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
                if len(treeList) <= 0:
                    break
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
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [root.val]

        def dfs(root):
            maxLeft = 0
            maxRight = 0
            if root.left:
                maxLeft = max(maxLeft, dfs(root.left))
            if root.right:
                maxRight = max(maxRight, dfs(root.right))
            
            maxVal[0] = max(maxVal[0], root.val + maxLeft + maxRight)
            return root.val + max(maxLeft,maxRight)
        
        dfs(root)
        return maxVal[0]

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPathSum(solution.createTree([-15,10,20,None,None,15,5,-5])) == 40
    assert solution.maxPathSum(solution.createTree([1,2,3])) == 6
    