# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGoodNodes = 0

        def dfs(node: Optional[TreeNode], lastGoodNode: int) -> None:
            nonlocal numGoodNodes
            
            if not node:
                return
            if node.val >= lastGoodNode:
                numGoodNodes += 1
                lastGoodNode = node.val
            
            dfs(node.left, lastGoodNode)
            dfs(node.right, lastGoodNode)
            
        dfs(root, root.val)

        return numGoodNodes