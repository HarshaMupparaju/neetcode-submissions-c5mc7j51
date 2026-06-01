class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # res = 0
        memo = {}

        ## O(2^n)
        #O(n^2) where n is the length of the string
        def dfs(temp: str, i: int) -> int:
            # nonlocal res

            if((temp, i) in memo):
                # res += memo[(temp, i)]
                # return res
                return memo[(temp, i)]

            if(i == len(s)):
                if(temp == t):
                    # res += 1
                    memo[(temp, i)] = 1
                    return 1
                memo[(temp, i)] = 0
                return 0
            
            res1 = dfs(temp + s[i], i + 1) #Add the current character
            res2 = dfs(temp , i + 1) #We ignore the current character

            memo[(temp, i)] = res1 + res2

            return res1 + res2


        res = dfs("", 0)

        return res