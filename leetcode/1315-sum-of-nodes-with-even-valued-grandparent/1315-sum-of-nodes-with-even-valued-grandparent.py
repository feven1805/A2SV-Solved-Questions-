# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    
        def dfs(node, parent, gp):
            if not node:
                return 0
            total = 0
            if gp % 2 == 0:
                total += node.val
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total
        return dfs(root,1,1)

        