# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = float('-inf') 
        def dfs(node):
            
            if not node:
                return 0
            
            left = max((dfs(node.left)), 0)
            right= max((dfs(node.right)), 0)
            self.maxx = max(self.maxx, left + node.val + right,left + node.val  , right + node.val, node.val )
            return max(left,right) + node.val
            
    
        dfs(root)
        return self.maxx    


            
               