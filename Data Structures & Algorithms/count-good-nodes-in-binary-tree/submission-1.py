# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)] #(node, int maximumSoFar)
        while stack:
            node, maximum = stack.pop()
            if node.left:
                stack.append((node.left, max(maximum, node.left.val)))
            if node.right:
                stack.append((node.right, max(maximum, node.right.val)))
            if node.val >= maximum:
                count += 1
        return count            
