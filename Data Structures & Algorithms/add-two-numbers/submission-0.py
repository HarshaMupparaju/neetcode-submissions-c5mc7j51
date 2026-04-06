# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)

        temp = res

        carry = 0

        while(l1 and l2):
            reminder = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10

            new_node = ListNode(reminder)
            temp.next = new_node

            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        
        l = None
        if(l1):
            l = l1
        elif(l2):
            l = l2
        
        while(l):
            reminder = (l.val + carry) % 10
            carry = (l.val + carry) // 10

            new_node = ListNode(reminder)
            temp.next = new_node

            l = l.next
            temp = temp.next
        
        if(carry):
            new_node = ListNode(carry)
            temp.next = new_node
        
            


        return res.next