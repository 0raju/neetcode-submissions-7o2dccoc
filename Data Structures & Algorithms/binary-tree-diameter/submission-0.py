# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1 
        count +=  max(self.maxDepth(root.left), self.maxDepth(root.right))
        return count
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
        diameter = leftdepth + rightdepth
        sub =  max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)        