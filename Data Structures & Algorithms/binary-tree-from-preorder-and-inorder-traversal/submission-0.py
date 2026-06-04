# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        preorderMap = {}
        inorderMap = {}
        for i, val in enumerate(preorder):
            preorderMap[val] = i
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        
        root = TreeNode()
        root.val = preorder[0]
        i = inorderMap[root.val]
        inorderLeft = inorder[:i]
        inorderRight = inorder[i+1:]
        i = 1
        while i < len(preorder) and preorder[i] in inorderLeft:
            i += 1
        preorderLeft = preorder[1:i]
        preorderRight = preorder[i:]

        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)

        return root