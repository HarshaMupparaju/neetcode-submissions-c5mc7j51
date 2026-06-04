class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n - 1): #A tree with n nodes has n - 1 edges
            return False
        
        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        
        for e in edges:
            a = e[0]
            b = e[1]

            adj_list[a].append(b)
            adj_list[b].append(a)
        
        vis = set()

        def dfs(node: int, parent: int) -> bool:
            if(node in vis): #A cycle is discovered
                return False
            
            vis.add(node)

            for nei in adj_list[node]:
                if(nei != parent): #Shouldn't go back the same path
                    if(dfs(nei, node) == False):
                        return False
            
            return True

        res = dfs(0, -1)

        if(res == False or len(vis) != n):
            return False
        
        return True