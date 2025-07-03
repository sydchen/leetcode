# @param {Integer[]} nums
# @return {Integer}
def max_sum_div_three(nums)
  dp0 = 0
  dp1 = -Float::INFINITY
  dp2 = -Float::INFINITY

  nums.each do |x|
    m = x % 3
    a0, a1, a2 = dp0, dp1, dp2

    case m
    when 0
      # 加到任何狀態都不改變 modulo
      dp0 = [a0 + x, dp0].max
      dp1 = [a1 + x, dp1].max
      dp2 = [a2 + x, dp2].max
    when 1
      dp0 = [a2 + x, dp0].max
      dp1 = [a0 + x, dp1].max
      dp2 = [a1 + x, dp2].max
    when 2
      dp0 = [a1 + x, dp0].max
      dp1 = [a2 + x, dp1].max
      dp2 = [a0 + x, dp2].max
    end
  end

  dp0
end

p max_sum_div_three([3,6,5,1,8])  # => 18  (3+6+1+8)
p max_sum_div_three([4])          # => 0
p max_sum_div_three([1,2,3,4,4])  # => 12  (1+3+4+4)

