# https://leetcode.com/discuss/57528/1-liner-in-ruby
# @param {String} s
# @return {String[]}
def find_repeated_dna_sequences(s)
  s.chars.each_cons(10).group_by(&:join).select { |_, group| group.size > 1 }.keys
end

puts find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
