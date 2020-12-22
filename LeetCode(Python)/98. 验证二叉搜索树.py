# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root, res):
            if not root:
                return res
            res = inorder(root.left, res)
            res.append(root.val)
            res = inorder(root.right, res)
            return res
        
        if not root:
            return True

        inorder_traversal = inorder(root, [])
        if len(inorder_traversal) == 1:
            return True

        is_valid_BST = True
        for i in range(1, len(inorder_traversal)):
            if inorder_traversal[i-1] >= inorder_traversal[i]:
                is_valid_BST = False
                break
        
        return is_valid_BST
