# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def buildTree(start, end):
            if start > end:
                return [None]

            res = []
            for i in range(start, end+1):
                leftTree = buildTree(start, i-1)
                rightTree = buildTree(i+1, end)

                for l in leftTree:
                    for r in rightTree:
                        root = TreeNode(val=i)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res

        return buildTree(1, n) if n else []