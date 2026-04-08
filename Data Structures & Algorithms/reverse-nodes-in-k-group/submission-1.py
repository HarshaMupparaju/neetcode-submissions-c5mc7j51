# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k == 1):
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        left = head
        right = head
        count = 0

        flag = 0

        while(right != None):
            if(count != k - 1):
                count += 1
                right = right.next
            else:
                start = left
                cur = left
                nxt = cur.next
                while(cur != right):
                    nxt_nxt = nxt.next
                    nxt.next = cur
                    cur = nxt
                    nxt = nxt_nxt
                
                start.next = nxt_nxt
                left = nxt_nxt
                right = nxt_nxt
                count = 0

                prev.next = cur
                prev = start
        
        return dummy.next