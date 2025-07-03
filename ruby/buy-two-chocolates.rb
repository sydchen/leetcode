def buy_choco(prices, money)
  min1 = Float::INFINITY
  min2 = Float::INFINITY

  prices.each do |p|
    if p <= min1
      min2 = min1
      min1 = p
    elsif p < min2
      min2 = p
    end
  end

  total = min1 + min2
  total <= money ? money - total : money
end

p buy_choco([1,2,2], 3) # => 3
p buy_choco([3,2,3], 3) # => 3
