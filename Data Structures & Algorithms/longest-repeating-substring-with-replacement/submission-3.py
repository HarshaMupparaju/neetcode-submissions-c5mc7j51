class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        res = 0

        def check(left: int, right: int) -> bool:
            max_so_far = 0
            for key in d:
                max_so_far = max(max_so_far, d[key])

            if(k >= (right - left + 1) - max_so_far):
                return True
            
            return False

        for r in range(len(s)):
            if(s[r] in d):
                d[s[r]] += 1
            else:
                d[s[r]] = 1
            
            while(not check(l, r)):
                print(l, r)
                d[s[l]] -= 1
                if(d[s[l]] == 0):
                    del d[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res