# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()

        q.append(root)

        res = []

        while(q):
            n = len(q)
            temp = []
            for i in range(n):
                front = q.popleft()

                temp.append(front.val)
                if(front.left):
                    q.append(front.left)
                if(front.right):
                    q.append(front.right)
            
            res.append(temp)
        
        return res

