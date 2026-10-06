# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return None

        # res = []
        # res.append(root.val)
        # def dfs(node):
        #     if not node:
        #         return None
        #     # res.append(node.val)

        #     if node.left and node.right:
        #         res.append(node.right.val)
        #     elif node.left:
        #         res.append(node.left.val)
        #     elif node.right:
        #         res.append(node.right.val)
            
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return res

        ###########
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
            
        return res