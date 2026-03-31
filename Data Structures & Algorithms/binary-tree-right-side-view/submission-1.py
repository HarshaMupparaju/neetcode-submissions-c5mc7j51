# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        #Base case
        if not root:
            return res

        q.append(root)

        while q:

            queue_len = len(q)

            for i in range(queue_len):
                cur_node = q.popleft()

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                
                if i == queue_len - 1:
                    res.append(cur_node.val)
        
        return res
