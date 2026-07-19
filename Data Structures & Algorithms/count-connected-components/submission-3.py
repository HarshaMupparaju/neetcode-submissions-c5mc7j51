class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}

        for ai, bi in edges:
            adj_list[ai].append(bi)
            adj_list[bi].append(ai)
        
        vis = set()
        res = 0

        def dfs(node: int) -> None:
            if(node in vis):
                return
            
            vis.add(node)

            for nei in adj_list[node]:
                dfs(nei)
            
            return

        for key in adj_list:
            if(key not in vis):
                dfs(key)
                res += 1
        
        return res