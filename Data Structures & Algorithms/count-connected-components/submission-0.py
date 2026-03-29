class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0]) #Undirected graph
        
        vis = [0] * n

        def dfs(i: int):
            if(vis[i] == 1):
                return
            vis[i] = 1

            for nei in adj_list[i]:
                dfs(nei)
            
            return

        res = 0
        for i in range(n):
            if(vis[i] == 0):
                res += 1
                dfs(i)
        
        return res