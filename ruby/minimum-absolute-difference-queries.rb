def min_difference(nums, queries)
  n = nums.length
  prefix = Array.new(n+1) { Array.new(101, 0) }
  (0...n).each do |i|
    prefix[i+1] = prefix[i].dup
    prefix[i+1][ nums[i] ] += 1
  end

  queries.map do |l, r|
    prev     = nil
    min_diff = Float::INFINITY

    (1..100).each do |v|
      cnt = prefix[r+1][v] - prefix[l][v]
      next if cnt == 0

      if prev
        diff = v - prev
        if diff == 1
          min_diff = 1
          break
        end
        min_diff = diff if diff < min_diff
      end
      prev = v
    end

    min_diff == Float::INFINITY ? -1 : min_diff
  end
end

nums    = [1,3,4,8]
queries = [[0,1],[1,2],[2,3],[0,3]]
p min_difference(nums, queries)  # => [2,1,4,1]

nums    = [4,5,2,2,7,10]
queries = [[2,3],[0,2],[0,5],[3,5]]
p min_difference(nums, queries)  # => [-1,1,1,3]

nums    =  [2,15,23,12,17,1]
queries = [[0,5]]
p min_difference(nums, queries)  # => [-1,1,1,3]

