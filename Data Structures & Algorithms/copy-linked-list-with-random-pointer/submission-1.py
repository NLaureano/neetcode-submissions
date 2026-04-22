"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        HM = {} #Node -> Copy
        if not head:
            return None
            
        def getDupe(node: Node) -> Node:
            copy = Node(node.val)
            if not node.next:
                copy.next = None
            else:
                copy.next = getDupe(node.next)
            HM[node] = copy
            return copy
        curr = getDupe(head)
        ret = HM[head]
        while curr:
            randomDest = head.random
            if randomDest:
                curr.random = HM[randomDest]
            head = head.next
            curr = curr.next
        
        return ret