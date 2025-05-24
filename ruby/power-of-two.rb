# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
  return false if n == 0
  return n > 0 && (n & n-1) == 0
end

puts is_power_of_two(0)
