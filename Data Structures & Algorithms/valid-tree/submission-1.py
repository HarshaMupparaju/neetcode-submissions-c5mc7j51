class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        vis = [0] * n

        def dfs(node: int, parent : int) -> bool:
            if(vis[node] == 1):
                return False
            
            vis[node] = 1

            for nei in adj_list[node]:
                if nei is not parent:
                    if not dfs(nei, node):
                        return False
            

            return True
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        res = dfs(0, -1)

        for i in range(n):
            if(vis[i] != 1):
                return False

        return res