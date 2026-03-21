# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # from collections import deque
        if not subRoot: return True
        if not root: return False
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                check = [(node, subRoot)]
                match = True
                while check:
                    n1, n2 = check.pop()
                    if not n1 and not n2:
                        continue
                    if not n1 or not n2 or n1.val != n2.val:
                        match = False
                        break
                    check.append((n1.left, n2.left))
                    check.append((n1.right, n2.right))
                if match: return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False