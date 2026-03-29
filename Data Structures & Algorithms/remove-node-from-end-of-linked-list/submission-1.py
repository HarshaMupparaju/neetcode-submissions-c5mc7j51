# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0)
        res.next = head

        total_nodes = 0

        temp = head

        while(temp != None):
            total_nodes += 1
            temp = temp.next

        temp = res
        count = 0
        while(temp != None):
            
            if(count == (total_nodes - n)):
                temp_next = temp.next
                temp_next_next = temp.next.next

                temp.next = temp_next_next

                temp_next = None
                return res.next

            count += 1
            temp = temp.next

    
        