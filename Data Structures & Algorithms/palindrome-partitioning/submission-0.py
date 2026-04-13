class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(st: str) -> bool:
            for i in range(len(st) // 2):
                if(st[i] != st[len(st) - 1 - i]):
                    return False
            
            return True

        def dfs(st: str, temp : List[str]) -> None:
            if(len(st) == 0):
                res.append(temp.copy())
                return
            
            for i in range(1, len(st) + 1):
                substring = st[:i]
                if(not is_palindrome(substring)):
                    continue
                temp.append(substring)
                dfs(st[i:], temp)
                temp.pop()
        

        dfs(s, [])

        return res

