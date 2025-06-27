def foreign_dictionary(words)
  nodes = words.flat_map(&:chars).uniq

  graph    = Hash.new { |h, k| h[k] = [] }
  indegree = Hash.new(0)
  nodes.each { |ch| indegree[ch] = 0 }

  words.each_cons(2) do |w1, w2|
    return "" if w1.length > w2.length && w1.start_with?(w2)

    # 找第一個不同的字元並建邊
    w1.chars.zip(w2.chars).each do |c1, c2|
      if c2 && c1 != c2
        graph[c1] << c2
        indegree[c2] += 1
        break
      end
    end
  end

  # Kahn’s algorithm
  queue = nodes.select { |ch| indegree[ch].zero? }
  order = []

  until queue.empty?
    u = queue.shift
    order << u
    graph[u].each do |v|
      indegree[v] -= 1
      queue << v if indegree[v].zero?
    end
  end

  order.size == nodes.size ? order.join : ""
end

puts(foreign_dictionary(["z","o"]))
puts(foreign_dictionary(["hrn","hrf","er","enn","rfnn"])) # hernf

