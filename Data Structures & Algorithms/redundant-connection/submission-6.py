class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # Number of nodes we have

        parent = [i for i in range(n + 1)] #Every node is its own parent initially
        rank = [1] * (n + 1) #Every node's rank is initially 1
    
        def find(node1: int) -> int:
            if(parent[node1] != node1): #Traverse upward
                parent[node1] = find(parent[node1])
            
            return parent[node1]


        def union(node1: int, node2: int) -> bool:
            p1 = find(node1)
            p2 = find(node2)
            if(p1 == p2): #Same component
                return False
            
            if(rank[p1] >= rank[p2]):
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            
            return True

        res = []

        for e in edges:
            ai = e[0]
            bi = e[1]
            # print(f'ai:{ai}, bi:{bi}, parent_ai:{find(ai)}, parent_bi:{find(bi)}')
            if(union(ai, bi) == False):
                # print(f'ai:{ai}, bi:{bi}, parent_ai:{find(ai)}, parent_bi:{find(bi)}')
                res = e
                break
            # print(f'ai:{ai}, bi:{bi}, parent_ai:{find(ai)}, parent_bi:{find(bi)}')
        
        return res

