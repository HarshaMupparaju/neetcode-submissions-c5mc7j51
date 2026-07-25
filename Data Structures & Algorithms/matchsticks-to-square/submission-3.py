class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #TC: O(4 * n)
        if(sum(matchsticks) % 4 != 0):
            return False
        
        n = sum(matchsticks) // 4

        temp = [0] * 4

        matchsticks.sort(reverse = True)

        def recurse(i: int) -> bool:
            # for j in range(len(temp)):
            #     if(temp[j] > n):
            #         return False

            if(i == len(matchsticks)):
                return True
            
            for j in range(len(temp)):
                if(temp[j] + matchsticks[i] <= n):
                    temp[j] += matchsticks[i]

                    if(recurse(i + 1)):
                        return True
                    temp[j] -= matchsticks[i]

            return False

        res = recurse(0)

        return res


        #TC: O(len(matchsticks) * sum(matchsticks)^4)
        # if(sum(matchsticks) % 4 != 0):
        #     return False
        
        # n = sum(matchsticks) // 4
        # dp = {}
        # def dfs(i: int, s1: int, s2: int, s3: int, s4: int) -> bool:
        #     if(s1 > n or s2 > n or s3 > n or s4 > n):
        #         return False
            
        #     if((i, s1, s2, s3, s4) in dp):
        #         return dp[(i, s1, s2, s3, s4)] 

        #     if(i == len(matchsticks)):
        #         return True
            
        #     res = (dfs(i + 1, s1 + matchsticks[i], s2, s3, s4) or 
        #             dfs(i + 1, s1, s2 + matchsticks[i], s3, s4) or 
        #             dfs(i + 1, s1, s2, s3 + matchsticks[i], s4) or 
        #             dfs(i + 1, s1, s2, s3, s4 + matchsticks[i]))
            
        #     dp[(i, s1, s2, s3, s4)] = res
        #     return res

        # res = dfs(0, 0, 0, 0, 0)

        # return res