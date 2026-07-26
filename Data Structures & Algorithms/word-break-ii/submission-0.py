class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        words = set()
        min_len = float('inf')
        max_len = float('-inf')

        for word in wordDict:
            words.add(word)
            
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))
        
        res = []
        temp = []
        def recurse(i: int) -> None:
            if(i == len(s)):
                res.append(' '.join(temp))
                return
            
            if(i > len(s)):
                return 

            for j in range(min_len, max_len + 1):
                if(i + j <= len(s) and s[i: i + j] in words):
                    temp.append(s[i : i + j])
                    recurse(i + j)
                    temp.pop()

        recurse(0)

        return res