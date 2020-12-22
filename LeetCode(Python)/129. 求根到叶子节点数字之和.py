# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ret = list()
        path = list()

        def dfs(root):
            if not root:
                return
            
            path.append(root.val)
            if not root.left and not root.right:
                ret.append(''.join(map(str, path[:])))
            dfs(root.left)
            dfs(root.right)
            path.pop()
        
        dfs(root)
        return sum(map(int, ret))