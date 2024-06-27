# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalidbst(root,minval,maxval):
            if not root:
                return True
            if root.val<=minval or root.val>=maxval:
                return False
            return isvalidbst(root.left,minval,root.val) and isvalidbst(root.right,root.val,maxval)
        return isvalidbst(root,-float('inf'), float('inf'))