def shortest_alternating_paths(n, red_edges, blue_edges)

  red_adj = Array.new(n) { [] }
  blue_adj = Array.new(n) { [] }
  red_edges.each { |u, v| red_adj[u] << v }
  blue_edges.each { |u, v| blue_adj[u] << v }

  answer = Array.new(n, -1)
  visited_red  = Array.new(n, false) # come from red
  visited_blue = Array.new(n, false) # come from blue

  queue  = [[0, 0, nil]] # from, dist, from which color
  while !queue.empty?
    node, dist, last_color = queue.shift

    # since edge weight 1
    answer[node] = dist if answer[node] == -1

    if last_color != 'red'
      red_adj[node].each do |adj_node|
        next if visited_red[adj_node]
        visited_red[adj_node] = true
        queue << [adj_node, dist + 1, 'red']
      end
    end

    if last_color != 'blue'
      blue_adj[node].each do |adj_node|
        next if visited_blue[adj_node]
        visited_blue[adj_node] = true
        queue << [adj_node, dist + 1, 'blue']
      end
    end

  end

  answer
end

p shortest_alternating_paths(3, [[0,1],[1,2]], [])

