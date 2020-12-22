# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                left_maxmum_node = root.left
                while left_maxmum_node.right:
                    left_maxmum_node = left_maxmum_node.right
                root.left = self.deleteNode(root.left, left_maxmum_node.val)
                root.val = left_maxmum_node.val
            else:
                root = root.left if root.left else root.right
        return root