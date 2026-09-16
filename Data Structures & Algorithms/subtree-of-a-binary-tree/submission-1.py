# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2):
                return False
            if (node1.val != node2.val):
                return False
            
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        def search(node, sb):
            if not node:
                return False
            if node.val == sb.val:
                if dfs(node, sb):
                    # self.res = True
                    return True
                else:
                    return search(node.left, sb) or search(node.right, sb)

                # if self.res:
                #     return True
            else:
                return search(node.left, sb) or search(node.right, sb)
            return False

        # self.res = False
        
        if search(root, subRoot):
            return True
        else:
            return False