# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.over_ten = 0
        self.add_number = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        head = res

        while l1 and l2:
            self.add_number = (l1.val + l2.val + self.over_ten) % 10
            self.over_ten = (l1.val + l2.val + self.over_ten) // 10
            l1 = l1.next
            l2 = l2.next
            node = ListNode(self.add_number)
            res.next = node
            res = res.next

        while l1:
            self.add_number = (l1.val + self.over_ten) % 10
            self.over_ten = (l1.val + self.over_ten) // 10
            l1 = l1.next
            node = ListNode(self.add_number)
            res.next = node
            res = res.next
        while l2:
            self.add_number = (l2.val + self.over_ten) % 10
            self.over_ten = (l2.val + self.over_ten) // 10
            l2 = l2.next
            node = ListNode(self.add_number)
            res.next = node
            res = res.next

        if self.over_ten == 1:
            node = ListNode(1)
            res.next = node

        return head.next
