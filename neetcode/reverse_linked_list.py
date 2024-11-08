from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def createLinkedList(self, list):
        head = ListNode(list[0])
        curr = head
        for i in list[1:]:
            curr.next = ListNode(i)
            curr = curr.next

        return head

    def createList(self, head):
        list = []
        curr = head
        while curr is not None:
            list.append(curr.val)
            curr = curr.next
        return list
            
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            last_node_reverse_1 = head.next
            reverse_1 = self.reverseList(head.next) 
            last_node_reverse_1.next = head
            head.next = None
            return reverse_1

if __name__ == "__main__":
    solution = Solution()
    head = solution.createLinkedList([0,1,2,3])
    assert solution.createList(solution.reverseList(head)) == [3,2,1,0]
        