"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node == None):
            return None

        old_to_new = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if(node in old_to_new):
                return old_to_new[node]
            
            temp = Node(node.val)
            
            old_to_new[node] = temp
            for nei in node.neighbors:
                temp.neighbors.append(dfs(nei))
            
            return temp

        res = dfs(node)

        return res
