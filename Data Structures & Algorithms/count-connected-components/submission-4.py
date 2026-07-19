class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]] # path compression
                node = parent[node]
            return node
        
        def union(node1: int, node2: int) -> int:
            p1 = find(node1)
            p2 = find(node2)

            if(p1 == p2):
                return 0 #Same component

            if(rank[p1] >= rank[p2]):
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            
            return 1


        res = n
        for ai, bi in edges:
            res -= union(ai, bi)

        return res

        # #TC: O(V + E); SC: O(V+E)
        # adj_list = {i : [] for i in range(n)}

        # for ai, bi in edges:
        #     adj_list[ai].append(bi)
        #     adj_list[bi].append(ai)
        
        # vis = set()
        # res = 0

        # def dfs(node: int) -> None:
        #     if(node in vis):
        #         return
            
        #     vis.add(node)

        #     for nei in adj_list[node]:
        #         dfs(nei)
        #     ty 
        #     return

        # for key in adj_list:
        #     if(key not in vis):
        #         dfs(key)
        #         res += 1
        
        # return res