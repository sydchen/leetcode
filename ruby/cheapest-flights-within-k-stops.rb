# @param {Integer} n
# @param {Integer[][]} flights
# @param {Integer} src
# @param {Integer} dst
# @param {Integer} k
# @return {Integer}

def find_cheapest_price(n, flights, src, dst, k)
  dist = Array.new(n, Float::INFINITY)
  dist[src] = 0

  (k + 1).times do
    new_dist = dist.clone

    flights.each do |u, v, w|
      next if dist[u] == Float::INFINITY
      new_dist[v] = [new_dist[v], dist[u] + w].min
    end

    dist = new_dist
  end

  dist[dst] == Float::INFINITY ? -1 : dist[dst].to_i
end

# ---- 範例測試 ----
puts find_cheapest_price(
  4,
  [[0,1,200],[1,2,100],[1,3,300],[2,3,100]],
  0, 3, 1
)   # => 500

puts find_cheapest_price(
  3,
  [[1,0,100],[1,2,200],[0,2,100]],
  1, 2, 1
)   # => 200
