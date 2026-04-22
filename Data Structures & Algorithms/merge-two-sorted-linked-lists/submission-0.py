# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        currN = None
        opp = None
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            res, currN = list1, list1
            opp = list2
        else:
            res, currN = list2, list2
            opp = list1
        
        nextN = currN.next
        nextNAlt = opp
        while nextN != None or nextNAlt != None:
            if nextN == None:
                currN.next = nextNAlt
                break
            elif nextNAlt == None:
                break

            if nextN.val <= nextNAlt.val:
                currN = currN.next
                nextN = currN.next
            else:
                currN.next = nextNAlt
                currN = currN.next
                nextNAlt = nextN
                nextN = currN.next
        return res
