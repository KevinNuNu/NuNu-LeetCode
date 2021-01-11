# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        move_step = length - k % length
        if length == 1 or move_step == length:
            return head
        
        tail.next = head

        for _ in range(move_step):
            head = head.next
            tail = tail.next
        
        tail.next = None

        return head