# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, postorder)

    def build(self, mid, post):
        if len(post) == 0:
            return
        r = TreeNode(post[-1])
        root_index = mid.index(post[-1])
        left_post = post[:root_index]
        right_post = post[root_index:-1]
        left_mid = mid[:root_index]
        right_mid = mid[root_index+1:]
        r.left = self.build(left_mid, left_post)
        r.right = self.build(right_mid, right_post)

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([9,3,15,20,7],[9,15,7,20,3]))