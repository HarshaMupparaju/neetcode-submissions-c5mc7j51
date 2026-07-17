class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        d = {}
        res = 0

        while(r < len(s)):
            
            if(s[r] in d):
                if(l < d[s[r]] + 1):
                    l = d[s[r]] + 1
                d[s[r]] = r
            else:
                d[s[r]] = r
            print(f"l:{l}, r:{r}")
            res = max(res, r - l + 1)

            r += 1
        
        return res