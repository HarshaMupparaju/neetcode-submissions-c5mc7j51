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

        left = float('-inf')
        right = float('inf')

        def validateBST(root: Optional[TreeNode], left: float, right: float) -> bool:
            if(root == None):
                return True

            if(root.val <= left or root.val >= right):
                return False
            
            left_tree = self.validateBST(root.left, float(left), float(root.val))

            right_tree = self.validateBST(root.right, float(root.val), float(right))

            return left_tree and right_tree

        return validateBST(root, left, right)