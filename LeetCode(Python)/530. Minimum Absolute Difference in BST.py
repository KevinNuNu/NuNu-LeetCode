# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        min_val = self.res[1] - self.res[0]
        for i in range(len(self.res) - 1):
            diff = abs(self.res[i + 1] - self.res[i])
            min_val = min(min_val, diff)
        return min_val

    def inorder(self, r):
        if r is None:
            return
        self.inorder(r.left)
        self.res.append(r.val)
        self.inorder(r.right)