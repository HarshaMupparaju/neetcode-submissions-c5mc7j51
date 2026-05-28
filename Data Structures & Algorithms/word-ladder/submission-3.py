class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = {}

        adj_list[beginWord] = []

        def check_one_char_away(word: str) -> List[int]:
            res = []

            def char_diff(word1: str, word2: str) -> int:
                count = 0
                for i in range(len(word1)):
                    if(word1[i] != word2[i]):
                        count += 1
                
                return count

            for k in adj_list:
                if(char_diff(word, k) == 1):
                    res.append(k)
            
            return res


        for word in wordList:
            
            adj_list[word] = []

            one_char_away = check_one_char_away(word)

            for temp in one_char_away:
                adj_list[temp].append(word)
                adj_list[word].append(temp)

        print(adj_list)
        # print(1/0)

        #DFS
        # vis = set()

        # def dfs(word: str, i: int) -> int:
        #     if(word == endWord):
        #         return i
            
        #     vis.add(word)

        #     res = float('inf')
        #     for nei in adj_list[word]:
        #         if(nei not in vis):
        #             res = min(dfs(nei, i + 1), res)
                
        #     vis.remove(word)
        #     return res


        # res = dfs(beginWord, 0)


        #BFS
        q = deque()

        q.append((beginWord, 0))

        res = 0

        vis = set()

        while(len(q) != 0):
            front, curr = q.popleft()

            # vis.add(front)

            if(front == endWord):
                res = curr
                break

            for nei in adj_list[front]:
                if(nei not in vis):
                    vis.add(nei)
                    q.append((nei, curr + 1))
            
            # vis.remove(front)



        if(res == 0):
            return 0

        return res + 1