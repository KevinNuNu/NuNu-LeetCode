# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total = 1
        child_list = []
        if root.left:
            child_list.append(root.left)
            total += 1
        if root.right:
            child_list.append(root.right)
            total += 1

        while child_list:
            root_list = child_list
            child_list = []
            for root in root_list:
                if root.left:
                    child_list.append(root.left)
                    total += 1
                if root.right:
                    child_list.append(root.right)
                    total += 1
        
        return total