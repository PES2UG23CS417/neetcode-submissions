# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        res = []
        q = deque()
        # visited = set()
        # visited.add(root)
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node and node.left:
                    left = node.left
                else:
                    left = None

                if node and node.right:
                    right = node.right
                else:
                    right = None

                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root