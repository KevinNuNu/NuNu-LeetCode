# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        tag = 'left_to_right'
        root_list = [root]

        while len(root_list) != 0:
            child_list = []
            child_val_res = []
            if tag == 'left_to_right':
                tag = 'right_to_left'
                for node in root_list:
                    if node.right:
                        child_list.append(node.right)
                        child_val_res.append(node.right.val)
                    if node.left:
                        child_list.append(node.left)
                        child_val_res.append(node.left.val)
            else:
                tag = 'left_to_right'
                for node in root_list:
                    if node.left:
                        child_list.append(node.left)
                        child_val_res.append(node.left.val)
                    if node.right:
                        child_list.append(node.right)
                        child_val_res.append(node.right.val)
            root_list = child_list[::-1]
            if len(child_val_res) != 0:
                res.append(child_val_res)
        
        return res