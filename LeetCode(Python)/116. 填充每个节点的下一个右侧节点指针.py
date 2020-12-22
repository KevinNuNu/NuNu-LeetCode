"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        child_list = []
        if root.left and root.right:
            child_list.append(root.left)
            child_list.append(root.right)
        
        while child_list:
            root_list = child_list
            for i in range(len(root_list)-1):
                root_list[i].next = root_list[i+1]
            child_list = []
            for node in root_list:
                if node.left and node.right:
                    child_list.append(node.left)
                    child_list.append(node.right)
                    
        return root