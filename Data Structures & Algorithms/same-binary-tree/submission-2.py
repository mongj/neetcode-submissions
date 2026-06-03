# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            # pop
            p1, q1 = queue.popleft()
            if (not p1 and not q1):
                continue
            elif not p1 or not q1:
                return False
            elif (p1 and q1 and p1.val != q1.val):
                return False
            # add left child
            queue.append((p1.left, q1.left))
            # add right
            queue.append((p1.right, q1.right))
        return True