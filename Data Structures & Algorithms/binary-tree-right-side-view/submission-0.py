# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            # index in res represents the level of the node
            # we use the level to check if that level has been seen before
            # we run dfs right to left to get right side view
            if not res or level >= len(res):
                res.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        
        dfs(root, 0)

        return res