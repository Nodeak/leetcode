# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, n1: Optional[ListNode], n2: Optional[ListNode]) -> Optional[ListNode]:
            
            if n1 is None or n2 is None:
                return n1 or n2
            
            if n1.val <= n2.val:
                n1.next = self.mergeTwoLists(n1.next, n2)
                return n1
            
            if n2.val <= n1.val:
                n2.next = self.mergeTwoLists(n1, n2.next)
                return n2
            
    
            