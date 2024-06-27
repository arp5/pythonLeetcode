# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def gn(root,maxv):
            if not root:
                return
            if root.val>=maxv:
                self.count+=1
            gn(root.left,max(maxv,root.val))
            gn(root.right,max(maxv,root.val))
        gn(root,root.val)
        return self.count
