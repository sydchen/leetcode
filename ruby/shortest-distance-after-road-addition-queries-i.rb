# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  dist = (0...n).to_a
  adj = Array.new(n) { [] }
  (0...n-1).each { |i| adj[i] << i + 1 }

  ans = []
  queries.each do |s, t|
    adj[s] << t
    if dist[s] + 1 < dist[t]
      dist[t] = dist[s] + 1

      queue = [t]
      while !queue.empty?
        x = queue.shift
        adj[x].each do |y|
          if dist[x] + 1 < dist[y]
            dist[y] = dist[x] + 1
            queue << y
          end
        end
      end
    end

    ans << dist[n-1]
  end

  ans
end

p shortest_distance_after_queries(5, [[2,4],[0,2],[0,4]]) # [3, 2, 1]
p shortest_distance_after_queries(4, [[0,3],[0,2]]) # [1, 1]
p shortest_distance_after_queries(5, [[0,2],[0,4]]) # [3, 1]
