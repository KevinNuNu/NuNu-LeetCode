# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0, head)
        p1 = dummy
        p = head

        count = 0
        stack = []
        while p:
            count += 1
            if count < m:
                p1 = p1.next
            elif count < n:
                stack.append(p)
            else:
                p2 = p.next
                stack.append(p)
                break
            p = p.next
        
        for node in stack[::-1]:
            p1.next = node
            p1 = node
        
        p1.next = p2

        return dummy.next