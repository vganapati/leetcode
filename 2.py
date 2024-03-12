# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    head_node = ListNode(0)
    tail_node = head_node
    carry = 0

    while l1 or l2 or carry>0:
        new_node = ListNode(0)
        tail_node.next = new_node
        new_node.val += carry
        if l1:
            new_node.val += l1.val
        if l2:
            new_node.val += l2.val
        

        carry = (new_node.val - new_node.val % 10)//10
        new_node.val = new_node.val % 10

        if l1:  
            l1 = l1.next
        if l2:
            l2 = l2.next
        tail_node = tail_node.next
    return head_node.next