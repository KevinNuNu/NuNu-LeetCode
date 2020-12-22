# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self._postorder(root, [])
    
    def _postorder(self, root, res):
        if not root:
            return res
        
        res = self._postorder(root.left, res)
        res = self._postorder(root.right, res)
        res.append(root.val)

        return res