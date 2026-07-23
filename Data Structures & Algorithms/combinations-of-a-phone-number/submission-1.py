class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Edge case
        if(len(digits) == 0):
            return []

        res = []
        #Digit to Letter mapping {int: []}
        mapping = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        #Go through each digit in digits and get all possible combinations
        def dfs(i: int, cur_str: str) -> None:
            #Base Case
            if(i == len(digits)):
                res.append(cur_str)
                return

            #Recursion
            for c in mapping[digits[i]]:
                dfs(i + 1, cur_str + c)
            
            return

        dfs(0, '')

        #Return
        return res