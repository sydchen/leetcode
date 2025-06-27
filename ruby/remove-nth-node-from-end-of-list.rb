class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end
# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  dummy = ListNode.new(0, head)
  fast = slow = dummy

  n.times do
    fast = fast.next
  end

  while fast.next
    fast = fast.next
    slow = slow.next
  end

  slow.next = slow.next.next
  dummy.next
end

def to_linkedlist(arr)
  dummy = ListNode.new(0)
  curr = dummy
  arr.each do |x|
    curr.next = ListNode.new(x)
    curr = curr.next
  end

  dummy.next
end

def display(list)
  while list
    print list.val
    list = list.next
  end
  puts
end

removed = remove_nth_from_end(to_linkedlist([1,2,3,4,5]), 2)
display(removed)

removed = remove_nth_from_end(to_linkedlist([3]), 1)
display(removed)

removed = remove_nth_from_end(to_linkedlist([1, 2]), 1)
display(removed)

