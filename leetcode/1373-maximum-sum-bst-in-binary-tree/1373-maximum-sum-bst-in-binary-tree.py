# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')

            lbst, lsum, lmin, lmax = dfs(node.left)
            rbst, rsum, rmin, rmax = dfs(node.right)

            if lbst and rbst and lmax < node.val < rmin:
                s = lsum + rsum + node.val
                self.ans = max(self.ans, s)
                return True, s, min(lmin, node.val), max(rmax, node.val)

            return False, 0, 0, 0

        dfs(root)
        return self.ans