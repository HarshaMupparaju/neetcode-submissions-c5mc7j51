# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while(cur != None):
            nxt = cur.next #Preload the next pointer
            cur.next = prev # Break the link
            
            #Do the 3 pointer update
            prev = cur
            cur = nxt
        
        return prev # when the 


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # n = 0
        # temp = head
        # while(temp != None):
        #     temp = temp.next
        #     n += 1

        slow = head
        fast = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            # if(fast.next == None):
            #     fast = fast.next
            # else:
            #     fast = fast.next.next
        
        mid = slow

        reversed_start = self.reverse_list(mid)

        # if(n % 2 == 1):
        #     reversed_start = self.reverse_list(mid.next)
        # else:
        #     reversed_start = self.reverse_list(mid)

        temp1 = head
        temp2 = reversed_start

        temp_count = 0
        while(temp2 != None):
            if(temp1.val != temp2.val):
                return False
            
            temp1 = temp1.next
            temp2 = temp2.next
            # temp_count += 1
        
        return True


