# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        temp = collections.deque()
        if not root:
            return res
        
        q.append(root)
        
        while len(q) > 0:
            ans = []
            while len(q) > 0:
                node = q.popleft()
                ans.append(node.val)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(ans)
            while len(temp) > 0:
                q.append(temp.popleft())
        
        return res