# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        if root is None:
            return res
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            to_add = []
            for i in range(size):
                node = q.popleft()
                to_add.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(to_add)
        return res