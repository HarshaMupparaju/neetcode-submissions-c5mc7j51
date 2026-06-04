class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []
        
        for pre in prerequisites:
            a = pre[0]
            b = pre[1]
            adj_list[a].append(b)
        
        path = set()
        done = set()
        res = []

        def dfs(i: int) -> bool:
            if(i in path):
                return False
            
            path.add(i)

            if(i in done):
                path.remove(i)
                return True
            
            done.add(i)

            for nei in adj_list[i]:
                if(dfs(nei) == False):
                    return False
            
            res.append(i)
            path.remove(i)

            return True


        for i in range(numCourses):
            if(i not in done):
                temp = dfs(i)
                if(temp == False):
                    print(i)
                    print(path)
                    return []
        
        return res