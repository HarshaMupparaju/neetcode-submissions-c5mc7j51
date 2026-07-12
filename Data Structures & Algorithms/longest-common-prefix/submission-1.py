class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        min_len = float('inf')
        for word in strs:
            min_len = min(min_len, len(word))

        for i in range(min_len):
            c = strs[0][i]
            for word in strs:
                if(word[i] != c):
                    return ''.join(res)
            
            res.append(c)
        
        return ''.join(res)

