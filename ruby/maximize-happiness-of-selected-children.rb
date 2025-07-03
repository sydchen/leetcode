# 734ms
def maximum_happiness_sum(happiness, k)
  # happiness.sort! { |a, b| b <=> a }
  sorted = happiness.sort.reverse # 直接回傳sorted array 會變成 206ms

  # 依序選前 k 個，計算每次有效的快樂值 (value - 已選次數)
  total = 0
  (0...k).each do |i|
    gain = sorted[i] - i
    break if gain <= 0

    total += gain
  end

  total
end

# 189ms, 204ms
def maximum_happiness_sum2(happiness, k)
  sorted = happiness.sort.reverse

  sum_happiness = 0
  t = 0

  sorted.each_with_index do |h, i|
    break if i >= k
    gain = h - i
    break if gain <= 0

    sum_happiness += h
    t += 1
  end

  # 扣除三角數：0 + 1 + ... + (t-1) = t*(t-1)/2
  penalty = t * (t - 1) / 2

  sum_happiness - penalty
end

p maximum_happiness_sum([1,2,3], 2)   # => 4
p maximum_happiness_sum([1,1,1,1], 2) # => 1
p maximum_happiness_sum([2,3,4,5], 1) # => 5
