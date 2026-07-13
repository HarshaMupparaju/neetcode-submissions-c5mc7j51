class MyHashSet:

    def __init__(self):
        self.hash_size = 1000001
        self.a = 1
        self.b = 1
        self.hash_set = [[] for _ in range(self.hash_size)]
        # self.hash_fn = lambda key: ((key % self.a) % self.b) 

    def add(self, key: int) -> None:
        self.hash_set[key].append(key)
        

    def remove(self, key: int) -> None:
        self.hash_set[key] = []
        

    def contains(self, key: int) -> bool:
        if(len(self.hash_set[key]) > 0):
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)