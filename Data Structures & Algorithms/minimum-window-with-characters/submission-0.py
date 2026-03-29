class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        d = {}

        for c in t:
            if(c in d):
                d[c] += 1
            else:
                d[c] = 1
        
        l = 0

        d_temp = d.copy()
        count = 0
        len_res = 1e7
        res = ''
        for r in range(n):
            if(s[r] in d_temp):
                d_temp[s[r]] -= 1
                # count += 1
            
            while(max(d_temp.values()) <= 0 ):
                print(s[l: r + 1])
                if(r - l + 1 < len_res):
                    res = s[l: r + 1]
                    
                    len_res = r - l + 1
                if(s[l] in d):
                    d_temp[s[l]] += 1
                    # count -= 1
                l += 1
        
        return res
            
            

