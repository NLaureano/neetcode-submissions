"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashMap = {}

        def clone(node: Node):
            if node in hashMap:
                return hashMap[node]
            
            copy = Node(node.val)
            hashMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
                
            return copy

        return clone(node)
        

