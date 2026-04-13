class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(s: str, temp: str) -> None:
            if(len(s) == 0):
                if(len(temp) != 0):
                    res.append(temp)
                return
            
            letters = d[s[0]]

            for letter in letters:
                dfs(s[1:], temp + letter)

        dfs(digits, '')

        return res