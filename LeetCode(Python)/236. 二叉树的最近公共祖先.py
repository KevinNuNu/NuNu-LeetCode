# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        self.GetNodePath(root, p, path1)
        path2 = []
        self.GetNodePath(root, q, path2)

        return self.GetLastCommonNode(path1, path2)
    
    def GetNodePath(self, root, target, path):
        if not root:
            return False
        
        # 在path中插入节点需要放在比较之前，否则会造成路径中没有p/q节点
        # 会使得p(q)是q(p)的祖先这种情况下无法得到正确答案
        path.append(root)
        if root == target:
            return True

        found = False

        child_list = []
        if root.left:
            child_list.append(root.left)
        if root.right:
            child_list.append(root.right)

        length = len(child_list)
        i = 0
        while not found and i < length:
            found = self.GetNodePath(child_list[i], target, path)
            i += 1
        
        if not found:
            path.pop()
        
        return found

    def GetLastCommonNode(self, path1, path2):
        ret = None
        length = min(len(path1), len(path2))
        for i in range(length):
            if path1[i] == path2[i]:
                ret = path1[i]
            else:
                break
        return ret