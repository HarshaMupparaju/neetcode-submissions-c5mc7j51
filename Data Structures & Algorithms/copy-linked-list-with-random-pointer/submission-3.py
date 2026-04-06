"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = Node(0)

        if not head:
            return None

        cur_node = Node(head.val)
        
        temp.next = cur_node

        d = {} #It will have old node(key) -> new_node (value)
        d[head] = cur_node 


        temp2 = head

        while(temp2):

            if temp2.next:
                if temp2.next in d:
                    cur_node.next = d[temp2.next]
                else:
                    new_node = Node(temp2.next.val)
                    cur_node.next = new_node
                    d[temp2.next] = cur_node.next
            else:
                cur_node.next = None
            
            if temp2.random:
                if temp2.random in d:
                    cur_node.random = d[temp2.random]
                else:
                    new_node = Node(temp2.random.val)
                    cur_node.random = new_node
                    d[temp2.random] = cur_node.random
            else:
                cur_node.random = None

            cur_node = cur_node.next
            temp2 = temp2.next


        return temp.next