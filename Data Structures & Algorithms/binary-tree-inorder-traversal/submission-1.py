# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Inorder Traversal
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                # left subtree exists so find Inorder Predecessor
                IP = curr.left
                while (IP.right and IP.right != curr):
                    IP = IP.right

                if IP.right is None:
                    # create the thread bc it hasn't been created
                    IP.right = curr
                    curr = curr.left # move left bc the thread to come back has been created so we can safely start traversing the left subtree

                elif IP.right == curr:
                    # means that thread already exists, hence left subtree has already been processed completely
                    # del the thread
                    IP.right = None
                    res.append(curr.val)
                    curr = curr.right
        
        return res