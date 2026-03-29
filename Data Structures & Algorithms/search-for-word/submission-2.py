class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        vis = [[0 for _ in range(n)] for _ in range(m)]

        def find_word(i: int, j: int, word_idx: int):
            if(i >= m or i < 0 or j >= n or j < 0):
                return False

            if(board[i][j] != word[word_idx] or vis[i][j] == 1):
                return False
            
            if(word_idx == len(word) - 1):
                return True
            
            vis[i][j] = 1
        
            #Up
            up =find_word(i - 1, j, word_idx + 1)

            #Right
            right = find_word(i, j + 1, word_idx + 1)

            #Left
            left = find_word(i, j - 1, word_idx + 1)

            #Down
            down = find_word(i + 1, j, word_idx + 1)

            vis[i][j] = 0

            return (up or left or down or right) 

        for i in range(m):
            for j in range(n):
                if(find_word(i, j, 0)):
                    return True

        
        return False

