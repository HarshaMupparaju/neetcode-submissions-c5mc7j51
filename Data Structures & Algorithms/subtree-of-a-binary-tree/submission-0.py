# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self, root:Optional[TreeNode], subRoot: Optional[Treenode]) -> bool:
        if(root == None and subRoot == None):
            return True
        elif(root == None or subRoot == None):
            return False

        if(root.val == subRoot.val):
            return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)
        
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and subRoot == None):
            return True
        elif(root == None or subRoot == None):
            return False

        if(root.val == subRoot.val):
            #Gotta check this
            # print(self.check(root, subRoot))
            # print(1/0)
            if(self.check(root, subRoot)):
                return True
            

        res = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return res

        
