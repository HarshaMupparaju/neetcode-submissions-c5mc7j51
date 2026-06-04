class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        
        for e in edges:
            a = e[0]
            b = e[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        vis = set()

        def dfs(node: int) -> None:
            if(node in vis):
                return
            
            vis.add(node)

            for nei in adj_list[node]:
                dfs(nei)
            
            return

        res = 0

        for i in range(n):
            if(i not in vis):
                dfs(i)
                res += 1
        
        return res