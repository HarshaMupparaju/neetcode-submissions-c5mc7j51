class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}

        for p in prerequisites:
            adj_list[p[0]].append(p[1])
        
        vis = set()

        def dfs(i: int) -> bool:
            if(adj_list[i] == []):
                return True
            
            if(i in vis):
                return False #cycle

            vis.add(i)
            for nei in adj_list[i]:
                if(not dfs(nei)):
                    return False
            
            adj_list[i] = []
            
            return True

        for i in range(numCourses):
            if(not dfs(i)):
                return False

        return True