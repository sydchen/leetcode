# 想法很簡單, 最小的2個數一定是分別放在num1和num2的開頭
# 以此類推
def split_num(num)
  digits = num.to_s.chars.map(&:to_i).sort

  a_digits = []
  b_digits = []
  toggle = true
  digits.each do |d|
    if toggle
      a_digits << d
    else
      b_digits << d
    end
    toggle = !toggle
  end

  a = a_digits.empty? ? 0 : a_digits.join.to_i
  b = b_digits.empty? ? 0 : b_digits.join.to_i

  a + b
end

p split_num(4325)   # => 59  （分成 24 + 35）
p split_num(687)    # => 75  （分成 7 + 68）
p split_num(100000) # => 1   （分成 00000 + 1 = 1）

