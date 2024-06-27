# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder = []
        def pre(root):
            if not root:
                return
            pre(root.left)
            preorder.append(root.val)
            pre(root.right)
        pre(root)
        return preorder[k-1]
        