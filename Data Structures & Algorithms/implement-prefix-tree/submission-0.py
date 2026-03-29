class PrefixNode:
    def __init__(self):
        self.children = {}
        self.last_node = False

class PrefixTree:

    def __init__(self):
        self.start = PrefixNode()
        

    def insert(self, word: str) -> None:
        node = self.start
        for i in range(len(word)):
            if(word[i] not in node.children):
                node.children[word[i]] = PrefixNode()

            if(i == len(word) - 1):
                node.children[word[i]].last_node = True
            
            node = node.children[word[i]]

        return  

    def search(self, word: str) -> bool:
        node = self.start
        res = False
        for i in range(len(word)):
            if(word[i] in node.children):
                node = node.children[word[i]]
            else:
                break
            if(i == len(word) - 1):
                if(node.last_node == True):
                    res = True

        return res

    def startsWith(self, prefix: str) -> bool:
        node = self.start
        res = True
        for i in range(len(prefix)):
            if(prefix[i] in node.children):
                node = node.children[prefix[i]]
            else:
                res = False
                break
            
        
        return res
        
        