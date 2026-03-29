class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        res_len = 1
        
        #Edge case
        # if(len(s) == 1):
        #     return s

        for i in range(len(s)):
            #Odd length
            l = i - 1
            r = i + 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if(r - l + 1 > res_len):
                    res = s[l: r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
            
            #Even length
            l = i
            r = i + 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if(r - l + 1 > res_len):
                    res = s[l: r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
        
        return res