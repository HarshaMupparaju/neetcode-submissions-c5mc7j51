# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []

        A = deque()
        A.append([root, 1])

        res = []

        temp = []

        while(len(A) > 0):
            node, current_level = A.popleft()

            temp.append(node.val)

            if(node.left != None):
                A.append([node.left, current_level + 1])
            
            if(node.right != None):
                A.append([node.right, current_level + 1])

            if(len(A) > 0 and A[0][1] > current_level):
                res.append(temp)
                temp = []
            
        res.append(temp)
        
        return res