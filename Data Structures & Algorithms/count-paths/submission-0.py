class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0

        def count_paths(i: int, j: int) -> None:
            nonlocal res

            #Out of bounds
            if(i >= m or j >= n):
                return
            
            #Base case
            if(i == m - 1 and j == n - 1):
                res += 1
                return
            
            dirs = [[0, 1], [1, 0]]

            for d in dirs:
                
                count_paths(i + d[0], j + d[1])
            
            return 
        
        count_paths(0, 0)

        return res