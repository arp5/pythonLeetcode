class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root:TreeNode, high, low):
        self.sum_nodes = 0
        def rsbst(root,high,low):
            if not root:
                return
            print(self.sum_nodes, root.val)
            if root.val < low:
                rsbst(root.right, high,low)
            elif root.val > high:
                rsbst(root.left, high,low)
            else:
                self.sum_nodes+=root.val
                rsbst(root.left, high,low)
                rsbst(root.right, high,low)
        rsbst(root,high,low)
        return self.sum_nodes

#root = [10,5,15,3,7,null,18], low = 7, high = 15
root = TreeNode(10)
#print(root.val)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
solution = Solution()

print(solution.rangeSumBST(root,15,7))