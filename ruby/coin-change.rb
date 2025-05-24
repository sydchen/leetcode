def coin_change(coins, amount)
  dp = Array.new(amount + 1, amount + 1)
  dp[0] = 0
  1.upto(amount) do |i|
    coins.each_with_index do |coin, j|
      if(coin <= i)
        dp[i] = [dp[i], dp[i-coin]+1].min
      end
    end
  end
  dp[amount] > amount ? -1 : dp[amount]
end

puts coin_change([1,2,5], 11)
