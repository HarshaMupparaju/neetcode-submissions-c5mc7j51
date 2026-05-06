class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if(c not in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        def search_helper(node, i) -> bool:
            if(i == len(word)):
                return node.end
            res = False
            if(word[i] == '.'):
                
                for child in node.children:
                    res = res or search_helper(node.children[child], i + 1)
                    if(res):
                        break
            else:
                if(word[i] not in node.children):
                    return False
                res = res or search_helper(node.children[word[i]], i + 1)

            return res

        res = search_helper(cur, 0)
        return res

