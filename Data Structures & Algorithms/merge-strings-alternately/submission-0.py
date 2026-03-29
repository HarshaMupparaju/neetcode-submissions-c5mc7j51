class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = ''

        for i in range(min(m, n)):
            res += word1[i]
            res += word2[i]
        
        if(n >= m):
            word = word1
        else:
            word = word2
        
        for i in range(min(m, n), len(word)):
            res += word[i]
        
        return res