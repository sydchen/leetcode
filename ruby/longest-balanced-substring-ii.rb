# @param {String} s
# @return {Integer}
def longest_balanced(s)
  n = s.length
  return 0 if n == 0

  max_len = 0

  # Case 1: 單一字母
  count = 1
  (1...n).each do |i|
    if s[i] == s[i-1]
      count += 1
    else
      max_len = [count, max_len].max
      count = 1
    end
  end
  max_len= [max_len, count].max

  # Case 2: 兩種不同字母
  pairs = [['a','b'], ['a','c'], ['b','c']]
  pairs.each do |x, y|
    diff = 0
    # seen 存 diff -> 最早 index（以原字串索引表示）
    seen = {0 => -1}
    (0...n).each do |i|
      ch = s[i]
      if ch == x
        diff += 1
      elsif ch == y
        diff -= 1
      else
        # 遇到第三個字母 — 必須重置（切段）
        diff = 0
        seen = {0 => i}  # 以 i 當成「前一個位置」，之後長度用 j - seen[diff]
        next
      end

      if seen.key?(diff) # 只要某個差值以前出現過，這兩個prefix之間的子串就有相等的 a 與 b
        max_len = [max_len, i - seen[diff]].max
      else
        seen[diff] = i
      end
    end
  end

  # Case 3: 三種字母同時存在：用 pair (b-a, c-a) 作為簽章
  ca = cb = cc = 0
  seen3 = {[0,0] => -1}
  s.chars.each_with_index do |ch, i|
    case ch
    when 'a' then ca += 1
    when 'b' then cb += 1
    when 'c' then cc += 1
    end

    key = [cb - ca, cc - ca]
    if seen3.key?(key)
      max_len = [max_len, i - seen3[key]].max
    else
      seen3[key] = i
    end
  end

  max_len
end

puts longest_balanced("abbac") # 4 "abba"
puts longest_balanced("zzabccy") # 4 "zabc"
puts longest_balanced("aba") # 2
puts longest_balanced("a") # 1
