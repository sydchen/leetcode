def reverse_vowels(s)
  vowels = "aeiouAEIOU"
  arr = s.chars
  l = 0
  r = arr.size - 1

  while l < r
    while l < r && !vowels.include?(arr[l])
      l += 1
    end
    while l < r && !vowels.include?(arr[r])
      r -= 1
    end

    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
  end

  arr.join
end

p reverse_vowels("hello")        # => "holle"
p reverse_vowels("leetcode")     # => "leotcede"
p reverse_vowels("aA")           # => "Aa"
