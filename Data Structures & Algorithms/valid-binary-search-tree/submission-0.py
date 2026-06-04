# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            if not node:
                return True
            return minVal < node.val < maxVal and isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)
        
        return isValid(root, float('-inf'), float('inf'))
        