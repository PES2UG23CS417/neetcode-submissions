# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root.val == p.val:
            return root
        elif root.val == q.val:
            return root
        
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if leftLCA and rightLCA:
            # we have found on both left and right which means that the current root has to be the lowest parent
            return root
        elif leftLCA:
            # that means both were found on the left only
            return leftLCA
        else:
            return rightLCA