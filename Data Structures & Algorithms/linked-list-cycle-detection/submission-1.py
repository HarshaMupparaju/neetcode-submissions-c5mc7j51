# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if(head == None):
            return False

        fast = head.next
        slow = head

        while(fast != None and slow != None):
            if(fast == slow):
                return True
            
            #Update pointers
            if(fast.next != None and slow.next != None):
                fast = fast.next.next
                slow = slow.next
            else:
                return False
        
        return False