class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring_start = 0
        d = {}
        res = -1
        for i in range(len(s)):
            if(s[i] in d):
                res = max(res, i - substring_start)
                temp = d[s[i]] + 1
                for j in range(substring_start, temp):
                    del d[s[j]]
                substring_start = temp
                d[s[i]] = i
                
            else:
                d[s[i]] = i
        
        res = max(res, len(s) - substring_start)
        
        return res