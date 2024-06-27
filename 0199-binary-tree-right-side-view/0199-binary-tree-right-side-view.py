# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue,ans = [],[]
        if not root:
            return ans
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                if not queue[0]:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
        return ans