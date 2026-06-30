def compare_version(version1, version2)
  list1 = version1.split('.').map(&:to_i)
  list2 = version2.split('.').map(&:to_i)

  max_len = [list1.length, list2.length].max

  (0...max_len).each do |i|
    num1 = list1[i] || 0
    num2 = list2[i] || 0

    return 1 if num1 > num2
    return -1 if num1 < num2
  end

  0
end

p compare_version("1.2", "1.10")
p compare_version("1.01", "1.001")
p compare_version("1.0", "1.0.0.0")
