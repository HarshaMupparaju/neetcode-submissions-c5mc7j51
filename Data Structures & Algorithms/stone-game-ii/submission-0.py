class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(alice: bool, i: int, M: int) -> int: #Alice's score
            if(i == len(piles)):
                return 0
            
            if((alice, i, M) in dp):
                return dp[(alice, i, M)]
            
            res = 0 if alice else float('inf')
            for X in range(1, 2 * M + 1):

                if(i + X > len(piles)):
                    break
                stones = sum(piles[i : i + X ])

                if(alice):
                    res = max(res, stones + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            
            dp[(alice, i, M)] = res
            return res

        res = dfs(True, 0, 1)

        return res