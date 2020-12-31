# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int: 
        pair = 0

        def dfs(root):
            nonlocal pair

            if not root.left and not root.right:
                # 如果该节点为叶子结点，则距离自己的距离为0
                return [0]
            
            # 如果左右子树为空，则表示没有叶子结点
            l = dfs(root.left) if root.left else []
            r = dfs(root.right) if root.right else []

            for i in l:
                for j in r:
                    # 注意这里的+2表示要加上连接root的距离2
                    if i + j +2 <= distance:
                        pair += 1
            
            # 把root的左右子树距离叶子结点的距离加上和自身的距离1
            # 返回的dist的定义即为该节点距离所有叶子结点的距离
            dist = [i + 1 for i in l + r]
            return dist

        dist = dfs(root)
        return pair