class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i

        for i in range(len(words) - 1):
            flag = False
            cur_word = words[i]
            next_word = words[i + 1]
        
            for j in range(min(len(cur_word), len(next_word))):
                if(d[cur_word[j]] < d[next_word[j]]):
                    flag = True
                    break
                if(d[cur_word[j]] > d[next_word[j]]):
                    return False

            if(not flag and len(cur_word) > len(next_word)):
                return False
        
        return True