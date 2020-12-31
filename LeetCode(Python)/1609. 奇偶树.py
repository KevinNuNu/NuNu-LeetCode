# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root.val & 1 == 0:
            return False
        
        child_node_list = []
        level = 1
        if root.left:
            if root.left.val & 1 != level:
                child_node_list.append(root.left)
            else:
                return False
        if root.right:
            if root.right.val & 1 != level:
                child_node_list.append(root.right)
            else:
                return False
        if not self.check(child_node_list, level):
            return False

        while child_node_list:
            root_list = child_node_list
            child_node_list = []
            level = (level + 1) & 1
            for root in root_list:
                if root.left:
                    if root.left.val & 1 != level:
                        child_node_list.append(root.left)
                    else:
                        return False
                if root.right:
                    if root.right.val & 1 != level:
                        child_node_list.append(root.right)
                    else:
                        return False
            if not self.check(child_node_list, level):
                return False
        
        return True
    
    def check(self, node_list, level):
        if len(node_list) <= 1:
            return True
        
        if level == 0:
            for i in range(1, len(node_list)):
                if node_list[i].val <= node_list[i-1].val:
                    return False
        else:
            for i in range(1, len(node_list)):
                if node_list[i].val >= node_list[i-1].val:
                    return False
        
        return True
