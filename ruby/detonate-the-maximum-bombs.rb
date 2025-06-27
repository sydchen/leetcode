=begin
如果炸彈i的半徑能覆蓋炸彈j, 圖中加一條有向邊 i -> j
對每個起點做一次 BFS／DFS，算出可到達節點的最大值
=end

# @param {Integer[][]} bombs   每筆 [x, y, r]
# @return {Integer}
def maximum_detonation(bombs)
  n = bombs.size
  adj = Array.new(n) { [] }
  bombs.each_with_index do |(x1, y1, r1), i|
    bombs.each_with_index do |(x2, y2, _), j|
      next if i == j
      dx = x1 - x2
      dy = y1 - y2

      if dx*dx + dy*dy <= r1*r1
        adj[i] << j
      end
    end
  end

  max_count = 0
  (0...n).each do |start|
    visited = Array.new(n, false)
    queue = [start]
    visited[start] = true
    count = 0

    until queue.empty?
      u = queue.shift
      count += 1
      adj[u].each do |v|
        next if visited[v]
        visited[v] = true
        queue << v
      end
    end

    max_count = [max_count, count].max
  end

  max_count
end

p maximum_detonation([[2,1,3],[6,1,4]])  # => 2
p maximum_detonation([[1,1,5],[10,10,5]]) # => 1

