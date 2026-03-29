class Solution:

    d = {}
    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res += f'{len(s)}#{s}'
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        
        while(i < len(s)):
            
            pound_marker = 0
            for j in range(i, len(s)):
                if(s[j] == '#'):
                    pound_marker = j
                    break
            
            n = int(s[i:pound_marker])
            res.append(s[pound_marker + 1: pound_marker + 1 + n])

            i = pound_marker + 1 + n
    
        return res