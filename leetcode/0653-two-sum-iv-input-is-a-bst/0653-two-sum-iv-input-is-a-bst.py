# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = False
        mydict = defaultdict(int)
    
        def myfunc(node):
            nonlocal ans
            if not node:
                return 0

            curr  = node.val
            if (k - curr) in mydict:
                ans = True
            else:
                mydict[curr] += 1

            myfunc(node.left)
            myfunc(node.right)
    
        myfunc(root)
        return ans

