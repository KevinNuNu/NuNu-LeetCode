# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        merged = ListNode(-1)
        # 将python中的变量名看作指针，此处head,merged指向同一地址
        head = merged
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            # 此处相当于将"merged"这个指针指向"merged.next"的地址上去
            # 而head指针始终是初始的头指针，指向初始的地址
            merged = merged.next
        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next

        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next

        return head.next
