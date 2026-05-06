class PrefixNode:
    def __init__(self, character, end = False, children=None):
        self.c = character
        self.end = end
        if not children:
            self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode(-1)
        

    def insert(self, word: str) -> None:
        temp = self.root
        for i in range(len(word) - 1):
            children = temp.children
            if(not word[i] in children):
                node = PrefixNode(word[i])
                children[word[i]] = node
            temp = children[word[i]]
        
        #Last charcter
        children = temp.children
        if(word[-1] in children):
            children[word[-1]].end = True
        else:
            node = PrefixNode(word[-1])
            node.end = True
            children[word[-1]] = node
        
        return


    def search(self, word: str) -> bool:
        temp = self.root
        for i in range(len(word) - 1):
            children = temp.children
            if(not word[i] in children):
                return False
            temp = children[word[i]]
        
        #Last character
        children = temp.children
        if(word[-1] in children):
            if(children[word[-1]].end == True):
                return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in range(len(prefix)):
            children = temp.children
            if(not prefix[i] in children):
                return False
            temp = children[prefix[i]]
        
        return True
        
        