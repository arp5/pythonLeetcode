# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def preorder(root,cursum,path):
            if not root:
                return
            if not root.left and not root.right:
                cursum+=root.val
                if cursum==targetSum:
                    path.append(root.val)
                    ans.append(path[:])
                    path.pop()
                    return
            path.append(root.val)
            preorder(root.left,cursum+root.val,path)
            preorder(root.right,cursum+root.val,path)
            path.pop()
        preorder(root,0,[])
        return ans

