# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        # dfs traverses the tree and returns the height
        # of the tree with node as the root.
        # it also updates maxDiameter as a side-effect
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            
            if not node:
                return 0
            leftSubtreeHeight = dfs(node.left)
            rightSubtreeHeight = dfs(node.right)
            currDiameter = leftSubtreeHeight + rightSubtreeHeight
            maxDiameter = max(maxDiameter, currDiameter)

            return 1 + max(leftSubtreeHeight, rightSubtreeHeight)

        dfs(root)

        return maxDiameter
            