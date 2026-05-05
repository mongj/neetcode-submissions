# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        lr = 0
        if root.left:
            lr += self.longestPath(root.left) + 1
        if root.right:
            lr += self.longestPath(root.right) + 1
        return max(l, r, lr)

    def longestPath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        return max(self.longestPath(root.left), self.longestPath(root.right)) + 1