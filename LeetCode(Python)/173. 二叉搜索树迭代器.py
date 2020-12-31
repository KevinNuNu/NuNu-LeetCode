# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = self.inorderTraversal(root)
        self.length = len(self.inorder)
        self.now = 0

    def inorderTraversal(self, root):
        ret = []

        def _inorder(root):
            if not root:
                return
            
            _inorder(root.left)
            ret.append(root)
            _inorder(root.right)

        _inorder(root)

        return ret

    def next(self) -> int:
        if self.length == 0:
            return None
        else:
            res = self.inorder[self.now]
            self.now += 1
            return res.val

    def hasNext(self) -> bool:
        return self.now < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()