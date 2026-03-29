class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        d = {}

        lengths = [len(current_string) for current_string in strs]

        min_l = min(lengths)

        for i in range(min_l):
            current_letter = strs[0][i]
            for j in range(1, len(strs)):
                if(strs[j][i] != current_letter):
                    return ans
            
            ans += current_letter
        
        return ans
