# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if(len(preorder) == 0 and len(inorder) == 0):
            return None
        temp = TreeNode(preorder[0])

        break_idx = 0
        for i in range(len(inorder)):
            if(inorder[i] == preorder[0]):
                break_idx = i
                break
        
        temp.left = self.buildTree(preorder[1: 1 + break_idx], inorder[:break_idx])
        temp.right = self.buildTree(preorder[1 + break_idx:], inorder[break_idx + 1:])

        return temp
