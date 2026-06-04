# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int | None:
            nonlocal k
            if not node:
                return
            res = dfs(node.left)
            if res:
                return res
            if k == 1:
                return node.val
            else:
                k -= 1
            res = dfs(node.right)
            if res:
                return res
        
        return dfs(root)