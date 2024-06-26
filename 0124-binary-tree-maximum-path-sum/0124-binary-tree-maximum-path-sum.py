# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -float('inf')
        def maxps(root):
            if not root:
                return 0
            left = max(0,maxps(root.left))
            right = max(0,maxps(root.right))
            self.maxsum = max(self.maxsum,root.val+left+right)
            return max(root.val+left,root.val+right)
        maxps(root)
        return self.maxsum