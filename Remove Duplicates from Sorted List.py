# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy1=head
        dummy2=head.next
        while dummy2:
            if dummy1.val == dummy2.val:
                dummy1.next = dummy2.next
            else:
                dummy1=dummy2
            dummy2=dummy2.next
        return head

