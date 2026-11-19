from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            # 先保存下一個節點，再反轉連線。
            next_node = current.next
            current.next = prev
            prev, current = current, next_node

        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = Solution().reverseList(head)
    values = []
    while reversed_head is not None:
        values.append(reversed_head.val)
        reversed_head = reversed_head.next

    assert values == [3, 2, 1]
    assert Solution().reverseList(None) is None
    print("Examples passed")
