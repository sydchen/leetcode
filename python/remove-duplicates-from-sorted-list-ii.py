from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next


def list_to_linked_list(lst):
    if not lst:
        return None

    dummy = ListNode(0)
    cur = dummy

    for num in lst:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

s = Solution()
root = s.deleteDuplicates(list_to_linked_list([1,2,3,3,4,4,5]))
print_list(root)
root = s.deleteDuplicates(list_to_linked_list([1,1,1,2,3]))
print_list(root)
