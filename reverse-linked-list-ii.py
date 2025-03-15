from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Head Insertion Method
# head: [1,2,3,4,5], left=2, right=4
# dummy → 1 → 2 → 3 → 4 → 5
# prev = 1, cur = 2
# lopp 1:
# temp = 3, remove(dummy → 1 → 2 → 4 → 5) then add back(dummy → 1 → 3 → 2 → 4 → 5)
# loop 2:
# temp = 4 remove(dummy → 1 → 3 → 2 → 5) and add back(dummy → 1 → 4 → 3 → 2 → 5)
# final dummy → 1 → 4 → 3 → 2 → 5
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head  # 如果鏈表為空 或 left == right，不需要反轉

        dummy = ListNode(0, head)
        prev = dummy

        # 找到 left 的前一個節點
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next  # `curr` 是 left 節點
        for _ in range(right - left):
            temp = curr.next  # 要移動的節點
            curr.next = temp.next  # 刪除 temp 節點
            temp.next = prev.next  # 插入 temp 到 prev 後面
            prev.next = temp  # 更新 prev 的指向

        return dummy.next


def list_to_linkedlist(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# 測試
head = list_to_linkedlist([1, 2, 3, 4, 5])
sol = Solution()
new_head = sol.reverseBetween(head, 2, 4)
print(linkedlist_to_list(new_head))  # [1, 4, 3, 2, 5]

