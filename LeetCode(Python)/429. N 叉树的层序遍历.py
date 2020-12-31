"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ret = [[root.val]]
        child_node_list = []
        for child_node in root.children:
            child_node_list.append(child_node)
        
        while child_node_list:
            root_list = child_node_list
            child_node_list = []
            level_ret = []
            for root in root_list:
                level_ret.append(root.val)
                for child_node in root.children:
                    child_node_list.append(child_node)
            ret.append(level_ret)

        return ret