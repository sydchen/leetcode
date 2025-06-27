# @param {Integer} buckets
# @param {Integer} minutes_to_die
# @param {Integer} minutes_to_test
# @return {Integer}
def poor_pigs(buckets, minutes_to_die, minutes_to_test)
  rounds = minutes_to_test / minutes_to_die
  # 一隻豬可表達的狀態數 = 輪數 + 1
  states = rounds + 1

  pigs = 0
  combinations = 1
  # 累乘直到能表示 >= buckets
  while combinations < buckets
    pigs += 1
    combinations *= states
  end

  pigs
end

p poor_pigs(4, 15, 15)
p poor_pigs(4, 15, 30)
