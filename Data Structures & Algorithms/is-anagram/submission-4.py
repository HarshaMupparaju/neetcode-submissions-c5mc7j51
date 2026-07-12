class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #TC: O(2n) and SC: O(n)
        #Add elements of string s to a dict
        d = {}

        for c in s:
            if(c in d):
                d[c] += 1
            else:
                d[c] = 1

        #Iterate over string t and delete and reduce the count in the dict, if there's a violation, then return False
        for c in t:
            if(c in d):
                d[c] -= 1
                if(d[c] == 0):
                    del d[c]
            else:
                return False
        


        #Check whether the dict is empty, if not return False
        if(len(d) != 0):
            return False
        
        return True
