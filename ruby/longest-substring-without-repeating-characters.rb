# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  str_len = s.length
  longest = Array.new(str_len, 0)
  for i in 0...str_len do
    next_same_char_index = s.index(s[i], i + 1)
    if next_same_char_index
      longest[i] = next_same_char_index - i
    else
      longest[i] = str_len - i
    end
  end

  p longest
  longest_len = 0
  current_longest_len = str_len
  for i in 0...str_len do
    # check distance
    current_longest_len = longest[i]
    right_border = i + longest[i]
    j = i + 1
    while(j < right_border) do
      if j + longest[j] < right_border
        right_border = j + longest[j]
      end
      current_longest_len = j - i + 1
      j += 1
    end
    longest_len = current_longest_len if current_longest_len > longest_len
  end
  longest_len
end
