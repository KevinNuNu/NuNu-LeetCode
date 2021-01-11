# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        p1 = head
        p2 = head
        p3 = dummy

        while p1.next:
            if p1.next.val != p1.val:
                if p1 == p2:
                    p1 = p1.next
                    p2 = p2.next
                    p3 = p3.next
                else:
                    p3.next = p1.next
                    p1 = p1.next
                    p2 = p1
            else:
                p1 = p1.next
        
        if p1 != p2:
            p3.next = None

        return dummy.next