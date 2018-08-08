# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.is_balance = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        self.height(root)

        return self.is_balance

    def height(self, root):
        if root is None:
            return 0

        height_left = self.height(root.left)
        height_right = self.height(root.right)

        if abs(height_left-height_right) > 1:
            self.is_balance = False
            return -1
        else:
            return max(height_left, height_right)+1



