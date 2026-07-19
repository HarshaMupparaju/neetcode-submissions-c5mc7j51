"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        node_mapping = {}

        def dfs(cur_node: Optional['Node']) -> Optional['Node']:
            if not cur_node:
                return None
            
            if(cur_node in node_mapping):
                return node_mapping[cur_node]
            
            new_node = Node(cur_node.val)
            node_mapping[cur_node] = new_node
            
            for nei in cur_node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node

        res = dfs(node)

        return res

