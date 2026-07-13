class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(-1) for _ in range(10**4)]
        self.hash_fn = lambda key: key % len(self.hash_set)
        

    def add(self, key: int) -> None:
        if(self.contains(key)):
            return
        cur_node = self.hash_set[self.hash_fn(key)]

        while(cur_node.next != None):
            cur_node = cur_node.next
        
        new_node = ListNode(key)
        cur_node.next = new_node

        return

    def remove(self, key: int) -> None:

        cur_node = self.hash_set[self.hash_fn(key)]

        while(cur_node.next and cur_node.next.val != key):
            cur_node = cur_node.next
        
        if(not cur_node.next):
            return

        cur_node.next = cur_node.next.next
        
        return

    def contains(self, key: int) -> bool:
        cur_node = self.hash_set[self.hash_fn(key)]

        while(cur_node and cur_node.val != key):
            cur_node = cur_node.next
        
        if(cur_node and cur_node.val == key):
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)