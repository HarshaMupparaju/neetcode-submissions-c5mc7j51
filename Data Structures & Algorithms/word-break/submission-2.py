class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [-1] * (len(s) + 1)
        dp[-1] = True

        def split_word(start: int) -> None:
            # if(start == len(s)):
            #     return True
            if(dp[start] != -1):
                return dp[start]
            
            res = False
            for word in wordDict:
                if(s[start: start + len(word)] == word):
                    res = split_word(start + len(word))
                    if(res == True):
                        break
            
            dp[start] = res
            return res


        split_word(0)

        return dp[0]