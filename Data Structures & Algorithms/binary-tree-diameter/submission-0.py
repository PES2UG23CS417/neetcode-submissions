# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr = root
        largest_D = 0
        def height(root):
            if root is None:
                return 0
            nonlocal largest_D
            leftH = height(root.left)
            rightH = height(root.right)
            diameter = leftH + rightH
            largest_D = max(largest_D, diameter)

            return 1 + max(leftH, rightH)
        
        height(root)

        return largest_D