# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy

        while p1 and p1.next:
            temp = p1.next.next
            p2.next = p1.next
            p1.next.next = p1
            p1.next = temp
            p2 = p1
            p1 = temp
        
        return dummy.next