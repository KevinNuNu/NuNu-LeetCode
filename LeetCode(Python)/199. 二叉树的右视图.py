# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ret = [root.val]
        child_list = []
        if root.right:
            child_list.append(root.right)
        if root.left:
            child_list.append(root.left)
        
        while child_list:
            root_list = child_list
            child_list = []
            ret.append(root_list[0].val)
            for root in root_list:
                if root.right:
                    child_list.append(root.right)
                if root.left:
                    child_list.append(root.left)
        
        return ret