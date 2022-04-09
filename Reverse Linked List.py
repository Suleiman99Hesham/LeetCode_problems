# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reversed_head = ListNode()
        while head:
            dummy=head.next
            head.next=reversed_head.next
            reversed_head.next=head
            head=dummy
        return reversed_head.next