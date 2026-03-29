# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur_head = res

        # cur_min = lists[0]
        # min_index = 0

        while(True):

            all_none = True
            #Find the first not None node
            for i, l in enumerate(lists):
                if(l != None):
                    cur_min = l
                    min_index = i
                    all_none = False
                    break
            
            if(all_none):
                break
            

            for i, l in enumerate(lists):
                if(l != None and cur_min.val > l.val):
                    cur_min = l
                    min_index = i
            
            print(cur_min.val, min_index)
            cur_head.next = cur_min
            # if(lists[min_index] != None):
            lists[min_index] = lists[min_index].next
            cur_min.next = None

            #Update cur_head
            cur_head = cur_head.next
        
        return res.next