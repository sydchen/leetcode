require 'set'

def reachable_nodes(n, edges, restricted)
  banned = restricted.to_set
  adj = Array.new(n) { [] }
  visited = Array.new(n, false)

  edges.each do |x, y|
    next if banned.include?(x) || banned.include?(y)
    adj[x] << y
    adj[y] << x
  end

  queue = [0]
  count = 0
  while !queue.empty?
    x = queue.shift
    count += 1
    visited[x] = true

    adj[x].each do |y|
      queue << y unless visited[y]
    end

  end

  count
end

p reachable_nodes(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [4,5])  # => 5
p reachable_nodes(7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1])# => 3
