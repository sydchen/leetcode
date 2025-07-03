def minimum_steps(s)
  swaps = 0    # 累計交換次數
  ones   = 0    # 已經掃到的黑球數

  # 從左到右掃描
  s.each_char do |c|
    if c == '1'
      ones += 1
    else
      # 遇到白球，要把它「與左邊所有黑球」交換過
      # 才能把所有黑球推到右側
      swaps += ones
    end
  end

  swaps
end

p minimum_steps("001011")  # => 5
p minimum_steps("11100")   # => 6
p minimum_steps("010101")  # => 3

