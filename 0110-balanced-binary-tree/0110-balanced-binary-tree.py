# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def maxheight(root):
        #     if not root:
        #         return 0
        #     return 1+ max(maxheight(root.left), maxheight(root.right))
        # if not root:
        #     return True
        # return abs(maxheight(root.left)-maxheight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        def height(root):
            if not root:
                return [True,0]
            left,right = height(root.left), height(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced,1+max(left[1], right[1])]
        return height(root)[0]