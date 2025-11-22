# n = 5, log_2{5} = 2.32, 取整數2
# 表示任何小於等於5的數, 2進位最高位數是2 (000 ~ 111) 共2^{2+1}種可能

# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  n = nums.length
  return n if n < 3
  b = Math.log2(n).floor
  1 << (b + 1)
end

p unique_xor_triplets([1,2])       # => 2
p unique_xor_triplets([3,1,2])     # => 4

