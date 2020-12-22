# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self._inorder(root, [])

    def _inorder(self, root, res):
        if not root:
            return res
        
        res = self._inorder(root.left, res)
        res.append(root.val)
        res = self._inorder(root.right, res)

        return res