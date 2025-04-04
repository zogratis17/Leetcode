# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None  # Return depth 0 and no LCA if node is None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_lca  # Return deeper subtree's LCA
            elif right_depth > left_depth:
                return right_depth + 1, right_lca  # Return deeper subtree's LCA
            else:
                return left_depth + 1, node  # If equal depth, current node is LCA

        return dfs(root)[1]
         # Time : O(N)
         # Space : O(H)