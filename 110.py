def isBalanced(root):
    def dfs(root):
        if root is None:
            return [True, 0]
        else:
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, 1 + max(left[1], right[1])]
        
    return dfs(root)[0]