# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Sol 1
        # p_inorder = []
        # q_inorder = []
        
        # def inorder(node, res):
        #     if node is None:
        #         res.append(None)
        #         return
        #     inorder(node.left, res)
        #     res.append(node.val)
        #     inorder(node.right, res)
        #     return res
        
        # p_inorder = inorder(p, [])
        # q_inorder = inorder(q, [])

        # print(p_inorder)
        # print(q_inorder)

        # if p_inorder == q_inorder:
        #     return True
        # return False
            
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if (node1 and not node2) or (node2 and not node1):
                return False
            
            if node1.val != node2.val:
                return False
            
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(p,q)