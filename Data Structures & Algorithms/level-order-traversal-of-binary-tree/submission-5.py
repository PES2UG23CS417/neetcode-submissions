# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        q1 = collections.deque()
        q2 = collections.deque()

        q1.append(root)

        while len(q1) > 0:
            tmp = []
            while len(q1)> 0:
                node = q1.popleft()
                tmp.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            res.append(tmp)
            while len(q2) > 0:
                q1.append(q2.popleft())
        
        return res
