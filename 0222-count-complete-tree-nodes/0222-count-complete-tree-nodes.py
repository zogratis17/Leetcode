# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.c=0
        def helper(root):
            if root:
                self.c+=1
                helper(root.left)
                helper(root.right)
            else:
                return
        helper(root)
        return self.c