# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        vorder = {}
        queue.append((root,0))
        minlevel,maxlevel = float('inf'), -float('inf')
        while queue:
            node,vlevel = queue.pop(0)
            minlevel = min(minlevel,vlevel)
            maxlevel = max(maxlevel,vlevel)
            if vlevel not in vorder:
                vorder[vlevel] = []
            vorder[vlevel].append(node.val)
            if node.left:
                queue.append((node.left,vlevel-1))
            if node.right:
                queue.append((node.right,vlevel+1))
        print(vorder)
        ans = []
        for level in range(minlevel,maxlevel+1):
            ans.append(vorder[level])
        return ans
