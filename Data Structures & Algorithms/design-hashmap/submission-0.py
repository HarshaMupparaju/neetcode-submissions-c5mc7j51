class MyHashMap:

    def __init__(self):
        self.d = [-1 for _ in range(2 ** 20)]

    def put(self, key: int, value: int) -> None:
        self.d[key % (2 ** 20)] = value
        return

    def get(self, key: int) -> int:
        return self.d[key % (2 ** 20)]

    def remove(self, key: int) -> None:
        self.d[key % (2 ** 20)] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)