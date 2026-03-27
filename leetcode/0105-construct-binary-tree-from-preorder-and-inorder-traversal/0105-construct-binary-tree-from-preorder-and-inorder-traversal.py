# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return 
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        leftInd = inorder[:idx]
        rightInd = inorder[idx + 1:]

        leftPre = preorder[1 : len(leftInd) +1]
        rightPre = preorder[len(leftInd) + 1:]

        root.left = self.buildTree(leftPre, leftInd)
        root.right = self.buildTree(rightPre, rightInd)
        return root

        