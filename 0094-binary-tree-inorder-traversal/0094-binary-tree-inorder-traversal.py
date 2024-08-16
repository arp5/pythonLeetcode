# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,ans= [],[]
        if not root:
            return []
        stack.append(root)
        node = root
        while stack:
            while node and node.left:
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            node = node.right
        print(ans)
        return ans



