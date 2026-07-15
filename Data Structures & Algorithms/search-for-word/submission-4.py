class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        def dfs(i: int, j: int, s: str) -> bool:
            if((i, j) in vis):
                return False
            
            vis.add((i, j))

            if(s == word):
                return True
            
            # if(i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[len(s)]):
            #     return False
            
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] #Up, Right, Down, Left

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if(ni < len(board) and ni >= 0 and nj < len(board[0]) and nj >= 0 and board[ni][nj] == word[len(s)]):
                    if(dfs(ni, nj, s + board[ni][nj])):
                        return True
            
            vis.remove((i, j))

            return False
            


        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    if(dfs(i, j, board[i][j])):
                        return True
        
        return False
                