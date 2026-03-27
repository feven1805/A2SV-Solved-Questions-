# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        summ = 0
        count = 0
        mydict = defaultdict(int)
        mydict[0] = 1

        def myfunc(node, summ):
            if not node:
                return 0
            nonlocal count
            summ += node.val
            if summ - targetSum in mydict:
                count += mydict[(summ - targetSum)]
            mydict[summ] += 1

            myfunc(node.left, summ)
            myfunc(node.right, summ)
            mydict[summ] -= 1
            if mydict[summ] == 0:
                del mydict[summ]
        myfunc(root, 0)
        return count

