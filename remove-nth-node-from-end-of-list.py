from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 使用 dummy 節點來統一處理刪除頭節點的情況
        fast = slow = dummy

        # 1. 讓 fast 先前進 n 步
        for _ in range(n):
            fast = fast.next

        # 2. 同時移動 fast 和 slow，直到 fast 到達鏈結串列的最後一個節點
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 3. 刪除 slow 的下一個節點
        slow.next = slow.next.next

        return dummy.next  # 返回新的頭節點



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
head = s.removeNthFromEnd(list_to_linked_list([1,2,3,4,5]), 2)
print_list(head)
head = s.removeNthFromEnd(list_to_linked_list([1]), 1)
print_list(head)
head = s.removeNthFromEnd(list_to_linked_list([1,2]), 1)
print_list(head)

