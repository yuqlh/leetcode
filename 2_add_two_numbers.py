# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        re = l
        while l1 or l2:
            if l1:
                l.val += l1.val
                l1 = l1.next
            if l2:
                l.val += l2.val
                l2 = l2.next
            if l.val>9:
                l.next = ListNode(1)
                l.val -= 10
            if (l.next == None) and (l1 or l2):
                l.next = ListNode(0)
            l = l.next
        return re
