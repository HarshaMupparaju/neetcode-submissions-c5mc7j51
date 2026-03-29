# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == None and q == None):
            return True
        elif( p == None and q != None):
            return False
        elif(p != None and q == None):
            return False
        
        left_res = False
        right_res = False
        if(p.val == q.val):
            left_res = self.isSameTree(p.left, q.left)
            right_res = self.isSameTree(p.right, q.right)

        return left_res and right_res