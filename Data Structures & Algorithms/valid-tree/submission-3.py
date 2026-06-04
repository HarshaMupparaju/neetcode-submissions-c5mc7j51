class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        
        for e in edges:
            a = e[0]
            b = e[1]

            adj_list[a].append(b)
            adj_list[b].append(a)
        
        path = set()
        done = set()

        def dfs(node: int, parent: int) -> bool:
            if(node in done):
                return True
            
            if(node in path):
                return False
            
            path.add(node)

            for nei in adj_list[node]:
                if(nei == parent):
                    continue
                if(dfs(nei, node) == False):
                    return False
            
            path.remove(node)
            done.add(node)
            
            return True

        # for i in range(n):
        #     if(i not in done):
        res = dfs(i, None)
        if(res == False):
            return False

        if(len(done) != n):
            return False
        
        return True