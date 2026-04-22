# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        middleIndex = inorder.index(preorder[0])
        leftTreeVals = inorder[:middleIndex]
        rightTreeVals = inorder[middleIndex + 1:]
        root.left = self.buildTree(preorder[1: middleIndex + 1], leftTreeVals)
        root.right = self.buildTree(preorder[middleIndex + 1:], rightTreeVals)
        return root
