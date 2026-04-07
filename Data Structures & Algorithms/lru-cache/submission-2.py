class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.d = {} #Maps key to ListNode

        #Connect head and tail, to prevent a lot of None edge cases
        self.head.prev = self.tail
        self.tail.next = self.head

    #Remove the node from the doubly linked list and handle the pointers
    def remove(self, node: ListNode) -> None:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        return 
    
    #Insert node at the start and handle the pointers
    def insert(self, node: ListNode) -> None:
        prev = self.head.prev
        nxt = self.head

        prev.next = node
        node.prev = prev

        nxt.prev = node
        node.next = nxt

        return 

    def get(self, key: int) -> int:
        if(key in self.d):
            #Push it to the front
            cur = self.d[key]
            self.remove(cur)
            self.insert(cur)

            return self.d[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.d):
            self.remove(self.d[key])
            del self.d[key]
            self.n -= 1
        
        new_node = ListNode(key, value)
        
        self.insert(new_node)
        self.d[key] = new_node
        self.n += 1

        while(self.n > self.capacity):
            del self.d[self.tail.next.key]
            self.remove(self.tail.next)
            self.n -= 1
        
        return
