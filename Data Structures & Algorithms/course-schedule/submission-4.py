class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            adj_list[a].append(b)

        done = set()
        path = set()

        def dfs(i: int) -> bool:
            if(i in path):
                return False #Already visited once in this path, so cycle
            
            if(i in done):
                return True #Already visited in another path and did not find any cycles
            
            path.add(i)

            if(i in done):
                return True

            for nei in adj_list[i]:
                if(dfs(nei) == False):
                    return False
            
            path.remove(i)
            done.add(i)

            return True

        for i in range(numCourses):
            if(i not in done):
                res = dfs(i)
                if(res == False):
                    return False
        
        return True

            

