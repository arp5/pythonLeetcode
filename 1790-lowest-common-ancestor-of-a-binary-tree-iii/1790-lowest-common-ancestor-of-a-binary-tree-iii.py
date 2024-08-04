"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def lca(root,p,q):
            if not root:
                return None
            if root ==p or root==q:
                return root
            left = lca(root.left,p,q)
            right = lca(root.right,p,q)
            if left and right:
                return root
            return left or right
        s = p
        while s.parent:
            s = s.parent
        root = s
        return lca(root,p,q)
            