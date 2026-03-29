class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        n = len(s1)

        def check_substring(d: Dict, s: str, n: int) -> bool:
            if(len(s) < n):
                return False

            for i in range(len(s)):
                if(s[i] not in d):
                    return False
                else:
                    if(d[s[i]] <= 0):
                        return False
                    else:
                        d[s[i]] -= 1
            
            return True

        for c in s1:
            if(c not in d):
                d[c] = 1
            else:
                d[c] += 1
        
        for i,c in enumerate(s2):
            if(c in d):
                temp = d.copy()
                if(check_substring(temp, s2[i : i + n], n)):
                    print(s2[i : i + n])
                    return True
        
        return False