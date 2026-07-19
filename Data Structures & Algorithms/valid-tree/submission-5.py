class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}

        for ai, bi in edges:
            adj_list[ai].append(bi)
            adj_list[bi].append(ai)
        
        vis = set()

        def dfs(node: int, parent_node: int) -> bool:
            if(node in vis):
                return False
            
            vis.add(node)

            for nei in adj_list[node]:
                if(nei != parent_node):
                    if(dfs(nei, node) == False):
                        return False
            
            return True
            


        res = dfs(0, -1)

        if(len(vis) != n):
            return False
        
        return res