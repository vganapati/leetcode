# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    if head:
        hare = head
        tortoise = head
        while tortoise.next and hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
    return False