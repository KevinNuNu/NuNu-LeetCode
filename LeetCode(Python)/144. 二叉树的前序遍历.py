# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self._preorder(root, [])

    def _preorder(self, root, res):
        if not root:
            return res
        
        res.append(root.val)
        res = self._preorder(root.left, res)
        res = self._preorder(root.right, res)

        return res