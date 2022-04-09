# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        if head.next == None and head.val == val:
            return None
        p=None
        res=head.next if head.val == val else head
        while head:
            if head.val == val:
                if p:
                    p.next=head.next
                else:
                    p=head.next
            head=head.next
        return res
