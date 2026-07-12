class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Iterate through each word and store a dict of characters
        dicts = []
        anagrams = {}
        res = []

        def check_anagram(word: str) -> int:

            for i,d in enumerate(dicts):
                temp = d.copy()
                flag = 0
                for c in word:
                    if(c in temp):
                        temp[c] -= 1
                        if(temp[c] == 0):
                            del temp[c]
                    else:
                        flag = 1
                        break
                
                if(not flag and len(d) != 0 and len(temp) == 0):
                    return i
                elif(not flag and len(word) == 0 and len(d) == 0):
                    return i
            
            return -1

        for word in strs:
            
            key = check_anagram(word)

            if(key != -1):
                # if(key in anagrams):
                anagrams[key].append(word)
                # else:
                #     anagrams[key] = [word]
                continue
            
            d = {}
            for c in word:
                if(c in d):
                    d[c] += 1
                else:
                    d[c] = 1
            
            dicts.append(d)
            anagrams[len(dicts) - 1] = [word]
        
        print(dicts)

        for k in anagrams:
            res.append(anagrams[k])

        return res