# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validateBST(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        if(root == None):
            return True

        if(root.val <= left or root.val >= right):
            return False
        
        left_tree = self.validateBST(root.left, left, root.val)

        right_tree = self.validateBST(root.right, root.val, right)

        return left_tree and right_tree

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True

        left = -1e10
        right = 1e10
        return self.validateBST(root, left, right)