# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        if list1==None and list2==None:
            return None
        if list1==None:
            return list2
        if list2==None:
            return list1
        p1=list1
        p2=list2
        p3=ListNode()
        merged_list=p3
        while True:
            if p1.val <= p2.val:
                p3.val=p1.val
                p1=p1.next
            else:
                p3.val=p2.val
                p2=p2.next

            if p1 == None and p2 == None:
                break
            elif p1 == None:
                p3.next=p2
                break
            elif p2 == None:
                p3.next=p1
                break
            p3.next=ListNode()
            p3=p3.next
        return merged_list
