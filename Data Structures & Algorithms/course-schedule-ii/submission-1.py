class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            adj_list[pre[0]].append(pre[1])

        path = set()
        done = set()

        res = []

        def dfs(i: int) -> bool:
            if(i in path):
                return False
            
            if(i in done):
                return True
            
            path.add(i)
            for nei in adj_list[i]:
                
                if( not dfs(nei)):
                    
                    return False
            
            path.remove(i)

            done.add(i)
            res.append(i)

            return True

        for i in range(numCourses):
            if(not dfs(i)):
                return []
        
        return res