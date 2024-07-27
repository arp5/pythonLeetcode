# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vorder = {}
        if not root:
            return vorder
        queue = []
        queue.append((root,0))
        maxlevel = -float('inf')
        minlevel = float('inf')
        while queue:
            node,level = queue.pop(0)
            maxlevel = max(maxlevel,level)
            minlevel = min(minlevel,level)
            if level not in vorder:
                vorder[level] = []
            vorder[level].append(node.val)
            if node.left:
                queue.append((node.left,level-1))
            if node.right:
                queue.append((node.right,level+1))
        print(vorder)
        ans = []
        for i in range(minlevel,maxlevel+1):
            ans.append(vorder[i])
        return ans
            