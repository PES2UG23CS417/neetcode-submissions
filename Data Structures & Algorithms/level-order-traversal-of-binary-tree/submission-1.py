# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q1 = collections.deque()
        q2 = collections.deque()
        q1.append(root)
        while len(q1) > 0:
            ans = []
            while len(q1) > 0:
                ele = q1.popleft()
                ans.append(ele.val)
                if ele.left:
                    q2.append(ele.left)
                if ele.right:
                    q2.append(ele.right)
            res.append(ans)
            while len(q2) > 0:
                q1.append(q2.popleft())
        
        return res