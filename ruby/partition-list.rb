# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end


# @param {ListNode} head
# @param {Integer} x
# @return {ListNode}
def partition(head, x)
  current = head
  ahead = []
  behind = []

  while(current) do
    if current.val < x
      node = ListNode.new(current.val)
      ahead.last.next = node if ahead.size > 0
      ahead << node
    else
      node = ListNode.new(current.val)
      behind.last.next = node if behind.size > 0
      behind << node
    end
    current = current.next
  end

  if ahead.empty?
    return behind.first
  elsif behind.empty?
    return ahead.first
  else
    ahead.last.next = behind.first
    return ahead.first
  end
end

# 1->4->3->2->5->2
list_nodes = []
prev_node = nil
%w{1 4 3 2 5 2}.each do |v|
  node = ListNode.new(v.to_i)
  prev_node.next = node if prev_node
  prev_node = node
  list_nodes << node
end

node =  partition(list_nodes.first, 3)
while(node) do
  puts node.val
  node = node.next
end
