# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 维护大小两个链表的方式
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        smallhead = ListNode(0, None)
        largehead = ListNode(0, None)
        small = smallhead
        large = largehead
        p = head

        while p:
            if p.val < x:
                small.next = p
                small = p
            else:
                large.next = p
                large = p
            p = p.next
        
        large.next = None
        small.next = largehead.next

        return smallhead.next

    # 四个指针的方式
    def partition1(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        p1 = dummy
        p2 = head

        # 找到第一个大于等于x的结点p2，以及其前一结点p1
        while p2.val < x and p2.next:
            p2 = p2.next
            p1 = p1.next
        
        # 把p2之后所有小于x的结点依次插入到p2之前
        p3 = p2
        p4 = p2.next
        while p4:
            if p4.val < x:
                temp = p4.next
                p1.next = p4
                p4.next = p2
                p3.next = temp
                p1 = p4
                p4 = temp
            else:
                p3 = p3.next
                p4 = p4.next
        
        return dummy.next