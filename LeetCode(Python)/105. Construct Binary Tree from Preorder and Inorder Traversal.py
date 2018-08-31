# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, inorder)

    def build(self, pre, mid):
        if len(pre) == 0:
            return
        r = TreeNode(pre[0])
        root_index = mid.index(pre[0])
        left_pre = pre[1:1+root_index]
        right_pre = pre[1+root_index:]
        left_mid = mid[:root_index]
        right_mid = mid[root_index+1:]
        r.left = self.build(left_pre, left_mid)
        r.right = self.build(right_pre, right_mid)

        return r
