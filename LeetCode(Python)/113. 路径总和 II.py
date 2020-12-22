# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret = list()
        path = list()
    
        def _pathSum(root, sum):
            if not root:
                return 

            path.append(root.val)
            sum -= root.val
            if not root.left and not root.right and sum == 0:
                ret.append(path[:])
            _pathSum(root.left, sum)
            _pathSum(root.right, sum)
            path.pop(-1)

        _pathSum(root, sum)
        return ret