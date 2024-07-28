# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inordera = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inordera.append(root.val)
            inorder(root.right)
        inorder(root)
        self.index = -1

    def next(self) -> int:
        self.index+=1
        return self.inordera[self.index]
        
    def hasNext(self) -> bool:
        return True if self.index!=len(self.inordera)-1 else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()