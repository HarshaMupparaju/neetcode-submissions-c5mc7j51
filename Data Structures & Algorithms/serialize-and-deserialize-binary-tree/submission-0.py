# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node: Optional[TreeNode]):
            if(node is None):
                res.append('N')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)

        s = ','.join(res)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        A = data.split(',')
        i = 0

        def dfs():
            nonlocal i

            if(A[i] == 'N'):
                i += 1
                return None
            
            cur_node = TreeNode(int(A[i]))
            i += 1
            
            cur_node.left = dfs()
            cur_node.right = dfs()

            return cur_node

        node = dfs()

        return node