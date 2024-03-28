from treeNode import TreeNode
def validateBST(root:TreeNode):
    def isV(root, high,low):
        if not root:
            return True
        if root.val<=low or root.val>=high:
            return False
        return isV(root.left,root.val,low) and isV(root.right,high,root.val)
    return isV(root,float('inf'), -float('inf'))
#root = [5,1,4,null,null,3,6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(validateBST(root))