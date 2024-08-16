# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inarray = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inarray.append(root.val)
            #print((inarray), len(inarray), k)
            if len(inarray) == k:
                return
            inorder(root.right)
        inorder(root)
        #print((inarray), len(inarray))
        return inarray[k-1]