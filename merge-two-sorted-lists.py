from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1

        head = prev = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        if list1 or list2:
            prev.next = list1 if list1 else list2

        return head.next

def makeList(lst):
    if len(lst) == 0: return None

    head = prev = ListNode(lst[0])
    for i in range(1, len(lst)):
        curr = ListNode(lst[i])
        prev.next = curr
        prev = curr
    return head

def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next

h1 = makeList([1,2,4])
h2 = makeList([1,3,4])
s = Solution()
s = printList(s.mergeTwoLists(h1, h2))

