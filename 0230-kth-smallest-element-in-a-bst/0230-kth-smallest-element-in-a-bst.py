# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inarray = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     inarray.append(root.val)
        #     if len(inarray) == k:
        #         return
        #     inorder(root.right)
        # inorder(root)
        # return inarray[k-1]
        #TC: O(N); SC:O(N)
        stack, ans = [],[]
        stack.append(root)
        node = root
        while stack:
            #print(stack)
            while node and node.left:
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            print(ans)
            if len(ans)==k:
                return ans[k-1]
            if node.right:
                stack.append(node.right)
            node = node.right
        return -1