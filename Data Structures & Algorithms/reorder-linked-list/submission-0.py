# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        mid = slow

        st = []

        # slow = slow.next
        while(slow != None):
            st.append(slow)
            slow = slow.next
        
        
        # print(1/0)

        temp = head

        while(temp != mid):
            temp_next = temp.next
            top = st.pop()
            temp.next = top
            top.next = temp_next
            temp = temp_next
        
        temp.next = None


        return 