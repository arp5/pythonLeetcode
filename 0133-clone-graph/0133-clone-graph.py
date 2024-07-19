"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap = {}
        if not node:
            return None
        def createNode(node):
            if node not in nodemap:
                newnode = Node(node.val)
                nodemap[node] = newnode
            return nodemap[node]
        def dfs(node):
            if not node:
                return None
            if node in nodemap:
                return nodemap[node]
            newnode = createNode(node)
            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            return nodemap[node]
        return dfs(node) 