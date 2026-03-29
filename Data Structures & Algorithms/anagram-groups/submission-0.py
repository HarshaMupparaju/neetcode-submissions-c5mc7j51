class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            if(sorted_string in d):
                d[sorted_string].append(i)
            else:
                d[sorted_string] = [i]
        
        res = []

        for k in d:
            temp = []
            for idx in d[k]:
                temp.append(strs[idx])
            
            res.append(temp)
        
        return res