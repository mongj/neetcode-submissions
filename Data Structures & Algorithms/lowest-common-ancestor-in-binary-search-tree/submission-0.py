# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p <= ancestor <= q (if p < q)
        if p.val < q.val:
            low, high = p, q
        else:
            low, high = q, p
        
        while root:
            if low.val <= root.val <= high.val:
                return root
            elif root.val > high.val:
                root = root.left
            else:
                root = root.right