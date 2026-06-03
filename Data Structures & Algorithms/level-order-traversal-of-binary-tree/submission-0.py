# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        while q:
            # pop all elements from the queue (same level)
            level = []
            for _ in range(len(q)):
                el = q.popleft()
                if el is not None:
                    level.append(el.val)
                    q.append(el.left)
                    q.append(el.right)
            if level:
                res.append(level)
                level = []
        return res