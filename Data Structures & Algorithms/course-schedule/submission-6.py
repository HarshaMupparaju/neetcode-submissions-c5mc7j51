class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}

        for course1, course2 in prerequisites:
            adj_list[course1].append(course2)
        
        vis = {} #0: in path, 1: visited

        def dfs(node: int) -> bool:
            if(node in vis and vis[node] == 0):
                return False
            
            if(node in vis and vis[node] == 1):
                return True
            
            vis[node] = 0

            for nei in adj_list[node]:
                if(dfs(nei) == False):
                    return False
            
            vis[node] = 1
        
            return True

        for i in range(numCourses):
            if(i not in vis):
                if(dfs(i) == False):
                    return False
        
        return True