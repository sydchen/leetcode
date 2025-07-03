=begin
最優路徑會把石頭分成「偶數索引」與「奇數索引」兩條交替路徑
在這種交錯上去下來的過程中，唯一可能的最大跳躍就是「跨過一塊石頭」的距離，即 stones[i] - stones[i-2]
=end

# @param {Integer[]} stones
# @return {Integer}
def max_jump(stones)
  n = stones.length
  return 0 if n < 2
  return stones[1] - stones[0] if n == 2

  max_dist = 0
  (2...n).each do |i|
    dist = stones[i] - stones[i - 2]
    max_dist = dist if dist > max_dist
  end

  max_dist
end

p max_jump([0,2,5,6,7])   # => 5
p max_jump([0,3,9])       # => 9
p max_jump([2,4])         # => 2
