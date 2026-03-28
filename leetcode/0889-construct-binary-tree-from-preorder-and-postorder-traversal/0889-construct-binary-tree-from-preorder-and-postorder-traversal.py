# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # root = preorder[0]
        # leaf = preorder[-1]
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        leftRoot = preorder[1]
        idx = postorder.index(leftRoot)
        
        leftPost = postorder[:idx + 1]
        rightPost = postorder[idx + 1:-1]
        
        leftPre = preorder[1 : len(leftPost) + 1]
        rightPre = preorder[len(leftPost) + 1:]
        
        root.left = self.constructFromPrePost(leftPre, leftPost)
        root.right = self.constructFromPrePost(rightPre, rightPost)
        
        return root