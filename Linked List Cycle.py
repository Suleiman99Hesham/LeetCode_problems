# Definition for singly-linked list.
from ast import While
from asyncio.windows_events import NULL
from turtle import pos


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head != NULL:
            if head.val == '*':
                return True
            head.val = '*'
            head = head.next
        return False