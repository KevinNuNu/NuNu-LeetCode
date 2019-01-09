# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.left = None
        self.right = None

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.left = L
        self.right = R
        self.inorder(root)
        return sum(self.res)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.left <= root.val <= self.right:
            self.res.append(root.val)
        self.inorder(root.right)
