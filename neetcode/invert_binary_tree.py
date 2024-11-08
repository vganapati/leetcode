from typing import Optional, List

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

    def treeToList(self, root: Optional[TreeNode]):
        if root == None:
            return []
        nodes = [root]
        vals = []
        while len(nodes) > 0:
            newNodes = []
            for node in nodes:
                if node == None:
                    vals.append(None)
                else:
                    vals.append(node.val)
                    if node.left is None and node.right is None:
                        pass
                    elif node.left is None and node.right is not None:
                        newNodes.append(node.left)
                        newNodes.append(node.right)
                    elif node.left is not None and node.right is None:
                        newNodes.append(node.left)
                    else:
                        newNodes.append(node.left)
                        newNodes.append(node.right)
            nodes = newNodes
        return vals


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        
        nodes = [root]

        while len(nodes) > 0:
            newNodes = []
            for node in nodes:
                # switch nodes
                tmp = node.left
                node.left = node.right
                node.right = tmp
                if node.left is not None:
                    newNodes.append(node.left)
                if node.right is not None:
                    newNodes.append(node.right)
            nodes = newNodes
        return root

if __name__ == '__main__':
    solution = Solution()

    root = [1,2]
    output = [1,None,2]
    assert solution.treeToList(solution.invertTree(solution.createTree(root))) == output

    root = [1,2,3,4,5,6,7]
    output = [1,3,2,7,6,5,4]
    breakpoint()
    assert solution.treeToList(solution.invertTree(solution.createTree(root))) == output

    root = [3,2,1]
    output = [3,1,2]
    assert solution.treeToList(solution.invertTree(solution.createTree(root))) == output

    root = []
    output = []
    assert solution.treeToList(solution.invertTree(solution.createTree(root))) == output

