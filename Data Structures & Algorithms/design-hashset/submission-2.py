class MyHashSet:

    def __init__(self):
        self.s = [0 for _ in range(1000001)]

    def add(self, key: int) -> None:
        self.s[key] = 1

    def remove(self, key: int) -> None:
        if(self.s[key] == 1):
            self.s[key] = 0
        return

    def contains(self, key: int) -> bool:
        if(self.s[key] == 1):
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)