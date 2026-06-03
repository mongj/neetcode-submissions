# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            return a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False

            subtreeInLeftChild = dfs(node.left)

            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True

            subtreeInRightChild = dfs(node.right)

            return subtreeInLeftChild or subtreeInRightChild

        return dfs(root)