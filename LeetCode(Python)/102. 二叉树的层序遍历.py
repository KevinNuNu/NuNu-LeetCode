# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        root_list = [root]

        while len(root_list) != 0:
            child_list = []
            child_val_res = []
            for node in root_list:
                if node.left:
                    child_list.append(node.left)
                    child_val_res.append(node.left.val)
                if node.right:
                    child_list.append(node.right)
                    child_val_res.append(node.right.val)
            root_list = child_list
            if len(child_val_res) != 0:
                res.append(child_val_res)
        
        return res