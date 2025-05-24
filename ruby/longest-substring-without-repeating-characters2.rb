# a brilliant solution from
# https://leetcode.com/discuss/74779/c-implementation-using-only-std-string
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  subs = ""
  max_len = 0
  for i in 0...(s.length) do
    at = subs.index(s[i])
    if at
      subs = subs[at+1..-1]
    end
    subs << s[i]
    max_len = subs.length > max_len ? subs.length : max_len
  end
  max_len
end

puts length_of_longest_substring("abcabcaa")
